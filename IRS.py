import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
# Optional: For PDF reading
import PyPDF2
import io

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")  # Adjust model name as needed

# Streamlit UI
st.set_page_config(page_title="Info Retrieval System", layout="centered")
st.title("🔎 Information Retrieval System using Gemini")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF or Text file (optional)", type=["pdf", "txt"])

context = ""
if uploaded_file:
    st.success("File uploaded successfully.")
    if uploaded_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(uploaded_file)
        for page in reader.pages:
            context += page.extract_text()
    elif uploaded_file.type == "text/plain":
        context = uploaded_file.read().decode("utf-8")

# Query input
query = st.text_input("Enter your question:")

# Send to Gemini
if st.button("Get Answer") and query:
    with st.spinner("Thinking..."):
        try:
            prompt = query
            if context:
                prompt = f"Use the following document to answer the question:\n\n{context[:8000]}\n\nQuestion: {query}"

            response = model.generate_content(prompt)
            st.subheader("📄 Answer:")
            st.write(response.text)

        except Exception as e:
            st.error(f"❌ Error: {e}")
