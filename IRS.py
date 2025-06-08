import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
import PyPDF2
import speech_recognition as sr
import pyttsx3
from io import BytesIO
from fpdf import FPDF
from unicodedata import normalize
import docx

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

# Setup Streamlit
st.set_page_config(page_title="Info Retrieval System", layout="centered")
st.title("🔎 Information Retrieval System using Gemini")

# Session State Initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "doc_context" not in st.session_state:
    st.session_state.doc_context = ""

if "doc_summary" not in st.session_state:
    st.session_state.doc_summary = ""

if "topic_summaries" not in st.session_state:
    st.session_state.topic_summaries = {}

if "audio_outputs" not in st.session_state:
    st.session_state.audio_outputs = {}

# Unicode fix for PDF
def sanitize_text(text):
    return normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")

# Audio format options
audio_format = st.selectbox("🎵 Select Audio Format", ["mp3", "wav", "ogg"])

# === File Upload ===
st.markdown("📂 **Upload your PDF, TXT, or DOCX files to get started**")
uploaded_files = st.file_uploader("Upload Files", type=["pdf", "txt", "docx"], accept_multiple_files=True)
if not uploaded_files:
    st.info("📌 *Please upload at least one file to enable question asking and summarization features.*")

combined_context = ""
if uploaded_files:
    for uploaded_file in uploaded_files:
        text = ""
        try:
            if uploaded_file.type == "application/pdf":
                reader = PyPDF2.PdfReader(uploaded_file)
                for page in reader.pages:
                    text += page.extract_text()
            elif uploaded_file.type == "text/plain":
                text = uploaded_file.read().decode("utf-8")
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                doc = docx.Document(uploaded_file)
                text = "\n".join([para.text for para in doc.paragraphs])

            combined_context += f"\n\n--- Document: {uploaded_file.name} ---\n{text.strip()}\n"
        except Exception as e:
            st.warning(f"Could not process {uploaded_file.name}: {e}")

    st.session_state.doc_context = combined_context[:8000]
    st.success(f"{len(uploaded_files)} files uploaded and processed.")

# === Summarization ===
with st.expander("🧾 Summarize Uploaded Documents"):
    st.markdown("Generate summaries of the uploaded documents using Gemini.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📃 Summarize Documents"):
            if st.session_state.doc_context:
                with st.spinner("Summarizing..."):
                    try:
                        summary_prompt = f"Summarize the following documents clearly and concisely:\n\n{st.session_state.doc_context}"
                        summary_response = model.generate_content(summary_prompt)
                        st.session_state.doc_summary = summary_response.text.strip()
                        st.success("✅ Summary generated.")
                    except Exception as e:
                        st.error(f"❌ Error: {e}")
            else:
                st.warning("Upload documents first.")

    with col2:
        if st.button("🧹 Clear Summary"):
            st.session_state.doc_summary = ""
            st.success("Summary cleared.")

    topic = st.text_input("🔍 Enter a specific topic to summarize:")
    if st.button("📌 Summarize Topic"):
        if topic and st.session_state.doc_context:
            with st.spinner(f"Summarizing topic: {topic}..."):
                try:
                    topic_prompt = (
                        f"From the following documents, generate a detailed and concise summary focused specifically "
                        f"on the topic '{topic}':\n\n{st.session_state.doc_context}"
                    )
                    topic_response = model.generate_content(topic_prompt)
                    topic_summary = topic_response.text.strip()
                    st.session_state.topic_summaries[topic] = topic_summary
                    st.markdown(f"### 🧠 Summary on: *{topic}*")
                    st.write(topic_summary)

                    st.download_button("📝 Download Topic Summary as TXT", topic_summary, f"summary_{topic}.txt", mime="text/plain")

                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial", size=12)
                    pdf.multi_cell(0, 10, sanitize_text(topic_summary))
                    pdf_bytes = pdf.output(dest="S").encode("latin1")
                    pdf_output = BytesIO(pdf_bytes)
                    st.download_button("📄 Download Topic Summary as PDF", pdf_output, f"summary_{topic}.pdf", mime="application/pdf")

                    engine = pyttsx3.init()
                    audio_path = f"topic_summary_{topic}.{audio_format}"
                    engine.save_to_file(topic_summary, audio_path)
                    engine.runAndWait()
                    with open(audio_path, "rb") as f:
                        audio_data = f.read()
                    st.audio(audio_data, format=f"audio/{audio_format}")
                    st.download_button("🔊 Download Topic Summary Audio", audio_data, file_name=audio_path, mime=f"audio/{audio_format}")
                except Exception as e:
                    st.error(f"❌ Error: {e}")
        elif not topic:
            st.warning("Please enter a topic before summarizing.")
        else:
            st.warning("Upload documents before using topic summarization.")

    if st.session_state.doc_summary:
        st.subheader("📌 Full Document Summary")
        st.write(st.session_state.doc_summary)

        st.download_button("📝 Download Full Summary as TXT", st.session_state.doc_summary, "full_document_summary.txt", mime="text/plain")

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, sanitize_text(st.session_state.doc_summary))
        pdf_bytes = pdf.output(dest="S").encode("latin1")
        pdf_output = BytesIO(pdf_bytes)
        st.download_button("📄 Download Full Summary as PDF", pdf_output, "full_document_summary.pdf", mime="application/pdf")

        engine = pyttsx3.init()
        audio_path = f"full_document_summary.{audio_format}"
        engine.save_to_file(st.session_state.doc_summary, audio_path)
        engine.runAndWait()
        with open(audio_path, "rb") as f:
            audio_data = f.read()
        st.audio(audio_data, format=f"audio/{audio_format}")
        st.download_button("🔊 Download Full Summary Audio", audio_data, file_name=audio_path, mime=f"audio/{audio_format}")

# === Chat Interface ===
st.subheader("💬 Ask Questions from the Document")

user_input = st.text_input(
    "Type your question here and press Enter",
    disabled=not bool(st.session_state.doc_context),
    placeholder="(Disabled until files are uploaded)"
)
if user_input:
    try:
        prompt = f"Based on the following context, answer the user's question.\n\nContext:\n{st.session_state.doc_context}\n\nQuestion: {user_input}"
        answer = model.generate_content(prompt).text.strip()
        st.session_state.chat_history.append((user_input, answer))
    except Exception as e:
        st.error(f"❌ Error: {e}")

if st.session_state.chat_history:
    st.subheader("📝 Conversation History")
    for i, (q, a) in enumerate(st.session_state.chat_history):
        st.markdown(f"**Q{i+1}:** {q}")
        st.markdown(f"**A{i+1}:** {a}")
        st.download_button(f"💾 Download A{i+1} as TXT", a, f"chat_answer_{i+1}.txt", mime="text/plain")
        engine = pyttsx3.init()
        audio_path = f"chat_answer_{i+1}.{audio_format}"
        engine.save_to_file(a, audio_path)
        engine.runAndWait()
        with open(audio_path, "rb") as f:
            audio_data = f.read()
        st.audio(audio_data, format=f"audio/{audio_format}")
        st.download_button(f"🔊 Download A{i+1} Audio", audio_data, file_name=audio_path, mime=f"audio/{audio_format}")
