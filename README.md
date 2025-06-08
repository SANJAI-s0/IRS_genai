# 🔎 Information Retrieval System using Gemini API

This is an intelligent Information Retrieval System built using **Python**, **Streamlit**, and **Google's Gemini API**. Users can upload PDF, DOCX, or text documents and ask questions — the app provides context-aware answers powered by Gemini 2.0 Flash.

---

## 📌 Use Case

- Upload any **PDF, DOCX, or TXT file**
- Ask **natural language questions** about the uploaded content
- Generate **summaries** of uploaded documents
- Export answers or summaries as **PDFs**
- Convert responses into **text-to-speech audio**

Common use cases include:

- 📘 Academic research or literature review  
- 🏫 Educational queries from notes or study material  
- 📄 Legal/medical/business document understanding  
- 🔉 Audio-based document briefing for accessibility  

---

## ⚙️ Installation

Follow these steps to set up and run the Information Retrieval System locally:

### 1. Clone the Repository

```bash
git clone https://github.com/SANJAI-s0/IRS_genai.git
cd IRS_genai
```

### 2. Create and Activate a Virtual Environment (Recommended)

```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a .env file in the root directory and add your Gemini API key:

```bash
GEMINI_API_KEY=your_actual_gemini_api_key
```

### 5. Run the Streamlit App

```bash
streamlit run IRS.py
```

Your Information Retrieval System will now be running in your browser at http://localhost:8501.

---

## 📦 Requirements

- Python 3.8 or higher
- Gemini API key (Get one from Google AI Studio)
- Internet connection

### requirements.txt

```bash

streamlit==1.37.0
python-dotenv==1.0.1
google-generativeai==0.5.4
PyPDF2==3.0.1
speechrecognition==3.10.1
pyttsx3==2.90
fpdf==1.7.2
python-docx==1.1.0

# Additional pakages
protobuf~=5.29.4
dotenv~=0.9.9

```

---

## 🔐 .env & .gitignore

### .env

```bash
GEMINI_API_KEY=your_actual_gemini_api_key
```

### .gitignore

```bash
.env
__pycache__/
*.pyc
*.mp3
*.wav
*.ogg
```

✅ This ensures your secret keys and compiled files are not pushed to GitHub.

---

## 🛠 Tech Stack

| Tool/Library        | Purpose                         |
| ------------------- | ------------------------------- |
| Python              | Core backend logic              |
| Streamlit           | Web-based UI framework          |
| PyPDF2              | PDF text extraction             |
| python-docx         | Word document parsing           |
| google-generativeai | Gemini LLM API access           |
| python-dotenv       | Environment variable management |
| pyttsx3             | Text-to-speech conversion       |
| fpdf                | Exporting summaries as PDFs     |

---

## 📝 License

MIT License — use freely with attribution

-----

## 🧠 How It Works

- 📁 User uploads one or more PDF, DOCX, or TXT files.
- 📄 Text is extracted and combined into a unified context.
- 👤 User can:
  - Ask natural language questions
  - Request a full or topic-specific summary
  - Download responses as PDF or listen via audio
- 🧠 The system constructs a prompt using document content and user input.
- 🚀 This prompt is sent to Gemini 2.0 Flash via API.
- 📤 The model returns a response, which is displayed in the UI.
- 📥 Users can download summaries or responses in multiple formats.

## 📬 Contact

Built by Sanjai
For suggestions or contributions, open an issue or a pull request on GitHub : https://github.com/SANJAI-s0/IRS_genai/issues

```bash
Let me know if you'd like me to:
- Add a section on **project structure**
- Include **deployment instructions** (e.g., Streamlit Cloud or Hugging Face)
- Attach this 'README.md' file to your project zip
```

I'm ready when you are!
