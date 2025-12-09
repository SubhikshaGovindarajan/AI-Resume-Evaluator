# AI Resume Evaluator (Streamlit + Ollama)

This application analyzes a candidate’s resume against a job description using a Large Language Model (LLM) and produces a structured JSON evaluation.  
It is built with Streamlit for the UI and uses a local LLM model (via Ollama) for scoring accuracy.

---

## 📂 Project Structure

AI-Resume-Evaluator/
- app.py  – Streamlit UI: PDF upload & resume input  
- main.py – LLM prompt creation and scoring logic  
- requirements.txt – Python dependencies  
- README.md – Project documentation  

---

## 🚀 Features

- Upload job description as a PDF  
- Paste resume text directly  
- Automatic PDF-to-text conversion using PyMuPDF (`fitz`)  
- LLM-powered resume evaluation  
- JSON-style output including:
  - Title match score  
  - Skills gap analysis  
  - Experience relevance  
  - Suggestions for improvement  
  - Overall compatibility score  

---

## 🧠 Tech Stack

- UI: Streamlit  
- AI Model: Llama 3.2 (via Ollama)  
- PDF Processing: PyMuPDF (`fitz`)  
- Language: Python  
- Output Format: JSON-style dictionary  

---

## 🧩 How It Works

1. User uploads a job description PDF.  
2. The app extracts text from the PDF.  
3. User pastes their resume text into the text area.  
4. Both job description and resume are sent to the LLM.  
5. The model returns a structured evaluation of how well the resume matches the job.

---

## ▶️ Run Locally

1. Install dependencies:  
   `pip install -r requirements.txt`  

2. Start the Streamlit app:  
   `streamlit run app.py`  

3. Make sure Ollama is installed and the model is available (for example `llama3.2:3b`), and that Ollama is running.

---

## 🛡️ Security

- Resumes are not stored on disk.  
- Evaluation happens locally using a local LLM model.  
- If you add cloud APIs later, use a `.env` file for secrets (do not commit it).

---

## 🔮 Future Enhancements

- Deploy on Streamlit Cloud or a similar platform.  
- Add visual skill-match charts.  
- Save evaluation history per user.  
- Allow resume PDF upload instead of plain text.

---

## 👩‍💻 Author

Created as part of learning NLP + LLM based application development.
