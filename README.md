# IRS_genai
An Information Retrieval System is a system designed to search, retrieve, and present information from a large collection of unstructured or semi-structured data (like documents, web pages, articles) based on user queries.


project:

markdown
Copy
Edit
# 🔎 Information Retrieval System using Gemini API

This project is a simple Information Retrieval System (IRS) built using **Python**, **Streamlit**, and the **Gemini API**. It allows users to upload a PDF or text document and ask questions. The system processes the content and queries Gemini to retrieve relevant answers.

---

## 📁 Project Structure

.
├── app.py # Main Streamlit app
├── .env # Stores Gemini API Key (not committed)
├── .gitignore # Ignores .env and other unnecessary files
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🚀 Features

- 📄 Upload PDF or Text documents
- ❓ Ask custom questions
- 🧠 Context-aware answers using Gemini API
- 🧼 Clean Streamlit UI
- 🔐 Secure API key via `.env`

---

## 🔧 Requirements

- Python 3.8+
- Gemini API key ([get yours here](https://aistudio.google.com/app/apikey))
- Internet connection

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up your .env file:

Create a file named .env and add your Gemini API key:

ini
Copy
Edit
GEMINI_API_KEY=your_actual_gemini_api_key
Run the app:

bash
Copy
Edit
streamlit run app.py
🔐 .env & .gitignore
.env
env
Copy
Edit
GEMINI_API_KEY=your_actual_gemini_api_key
.gitignore
gitignore
Copy
Edit
.env
__pycache__/
*.pyc
🧠 How It Works
User uploads a PDF or text file.

File content is extracted and stored as context.

User submits a question.

The app builds a prompt combining the file context + question.

Prompt is sent to Gemini 2.0 Flash via API.

Response is displayed in the Streamlit UI.

🛠 Tech Stack
Python

Streamlit

Google Generative AI (google.generativeai)

PyPDF2

dotenv

✅ Future Improvements
Semantic search with FAISS or ChromaDB

Support for multiple files

Add conversation memory / chat history

Response summarization

UI theming with Streamlit components

📝 License
MIT License. Use freely with attribution.

📬 Contact
For any questions, feel free to reach out via GitHub Issues.

yaml
Copy
Edit

---

Let me know if you'd like me to tailor this for deployment (like on Streamlit Cloud or Render) or want badges/shields at the top.
