# AI Resume Evaluator (Streamlit + Ollama)

This application analyzes a candidate’s resume against a job description using a Large Language Model (LLM) and produces a **structured JSON evaluation**.  
Built with **Streamlit** for UI and a local LLM model (via Ollama) for scoring accuracy.

---
📂 Project Structure
AI-Resume-Evaluator/
│
├── app.py             # Streamlit UI: PDF upload & resume input
├── main.py            # LLM prompt creation + scoring logic
├── requirements.txt   # Dependencies
└── README.md

---

## 🚀 Features

- Upload **Job Description** as PDF
- Paste **Resume Text** directly
- Automatic PDF-to-text conversion using PyMuPDF (`fitz`)
- LLM-powered resume evaluation
- Output is a structured JSON containing:
  - 🔹 Title Match Score
  - 🔹 Skills Gap Analysis
  - 🔹 Experience Relevance
  - 🔹 Suggestions for Improvement
  - 🔹 Overall Compatibility Score

---

## 🧠 Tech Stack

| Area | Technology |
|------|------------|
| UI | Streamlit |
| AI Model | Llama 3.2 (via Ollama) |
| PDF Processing | PyMuPDF (`fitz`) |
| Backend Logic | Python |
| Output Format | JSON |

---

## 🧩 How It Works

1️⃣ User uploads a **Job Description PDF**  
2️⃣ PDF text is extracted using PyMuPDF  
3️⃣ User pastes resume text  
4️⃣ Both are passed to an LLM model  
5️⃣ Output JSON is displayed on screen

---

## ▶️ Run Locally

Install dependencies:
```
pip install -r requirements.txt

Start the app:
streamlit run app.py

Make sure Ollama is running with the required model:
ollama run llama3.2:3b

🛡️ Security
No resumes stored on disk

Runs fully offline using local LLM

.env recommended for secret configs if cloud APIs used

🔮 Future Enhancements
Deploy to Streamlit Cloud with API-based LLM (Groq / Gemini)

Add resume skill visualization charts

Save evaluation history for users

Accept resume PDF upload instead of plain text

📌 Requirements
All dependencies listed in requirements.txt.

👩‍💻 Author
Created as part of learning NLP + LLM application development.
