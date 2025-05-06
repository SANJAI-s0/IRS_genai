# IRS_genai
An Information Retrieval System is a system designed to search, retrieve, and present information from a large collection of unstructured or semi-structured data (like documents, web pages, articles) based on user queries.


# 🔎 Information Retrieval System using Gemini API

This is an intelligent Information Retrieval System built with **Python**, **Streamlit**, and **Google's Gemini API**. Users can upload PDF or text documents and ask questions. The system uses the document content to generate context-aware answers via Gemini's large language models.

---

## 📌 Use Case

- Upload any **PDF or TXT file**
- Ask **natural language questions** about the uploaded content
- Get **accurate, context-aware responses** from Gemini 2.0 Flash
- Useful for:
  - Research and literature review
  - Educational Q&A from notes or eBooks
  - Document understanding in legal, business, or medical fields

---

## 📦 Requirements

- Python 3.8 or above
-- streamlit>=1.30.0
-- python-dotenv>=1.0.0
-- google-generativeai>=0.3.0
-- PyPDF2>=3.0.1
- Google Gemini API key (get it [here](https://aistudio.google.com/app/apikey))

---

## ⚙️ Installation

Follow these steps to set up and run the project:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows

### 3. Install dependencies

```bash
pip install -r requirements.txt

### 4. Create a .env file

```bash
GEMINI_API_KEY=your_actual_gemini_api_key

### 5. Run the Streamlit app

```bash
streamlit run app.py

---

## 🧠 How It Works

- The user uploads a document (PDF or TXT)
- The content is extracted and stored as context
- The user enters a question in the input field
- A prompt is generated using both the document and the question
- The prompt is sent to Gemini 2.0 Flash
- The model returns a context-aware answer, displayed in the app

---

## 🔐 .env & .gitignore

### .env

```bash
GEMINI_API_KEY=your_actual_gemini_api_key

### .gitignore

```bash
.env
__pycache__/
*.pyc

# ⚠️ Keep your .env file private by ensuring it's listed in .gitignore

---

## 🛠 Tech Stack / Tools Used

| Tool/Library          | Purpose                             |
| --------------------- | ----------------------------------- |
| Python                | Core language                       |
| Streamlit             | Web-based UI                        |
| PyPDF2                | PDF text extraction                 |
| `google.generativeai` | Gemini API integration              |
| dotenv                | Secure API key management           |
| Git + GitHub          | Version control and project hosting |

---

## 📁 Project Structure

```bash
.
├── app.py                 # Main Streamlit application
├── .env                  # Gemini API key (ignored)
├── .gitignore            # To prevent sensitive files from being committed
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

---

## 📝 License

This project is licensed under the MIT License.
Feel free to use, share, and modify with attribution.

---

## 📬 Contact

For issues or ideas, open an issue on:
https://github.com/SANJAI-s0/IRS_genai
EOT

echo "✅ Project setup complete!"
echo "📁 Next: Add your Gemini API key in the .env file."
echo "▶️ Run the app with: streamlit run app.py"

```bash
#yalm

---

### 📌 To Use:

1. Save this script as `setup.sh`
2. Run it in your terminal:

```bash
chmod +x setup.sh
./setup.sh



---