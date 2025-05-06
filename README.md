# 🔎 Information Retrieval System using Gemini API

This is an intelligent Information Retrieval System built using **Python**, **Streamlit**, and **Google's Gemini API**. Users can upload PDF or text documents and ask questions — the app provides context-aware answers powered by Gemini 2.0 Flash.

---

## 📌 Use Case

- Upload any **PDF or TXT file**
- Ask **natural language questions** about the uploaded content
- Get **accurate, context-sensitive responses** via Gemini LLM

Common use cases include:

- 📘 Academic research or literature review  
- 🏫 Educational queries from notes or study material  
- 📄 Legal/medical/business document understanding  

---

## ⚙️ Installation

Follow these steps to set up and run the Information Retrieval System locally:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
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
streamlit run app.py
```

Your Information Retrieval System will now be running in your browser at http://localhost:8501.

---

## 📦 Requirements

- Python 3.8 or higher
- Gemini API key (Get one)
- Internet connection

### requirements.txt

```bash
streamlit>=1.30.0
python-dotenv>=1.0.0
google-generativeai>=0.3.0
PyPDF2>=3.0.1
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
```

✅ This ensures your secret keys and compiled files are not pushed to GitHub.

---

## 🛠 Tech Stack

| Tool/Library        | Purpose                         |
| ------------------- | ------------------------------- |
| Python              | Core backend logic              |
| Streamlit           | Web-based UI framework          |
| PyPDF2              | PDF text extraction             |
| google-generativeai | Gemini LLM API access           |
| python-dotenv       | Environment variable management |

---

## 📝 License

MIT License — use freely with attribution

-----

## 🧠 How It Works

- User uploads a PDF or TXT file.
- Text is extracted and used as context.
- User types a question into the interface.
- The system builds a prompt from the document question.
- The prompt is sent to Gemini 2.0 Flash via the API.
- The model returns a response, shown in the UI.