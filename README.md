# 🤖 InterviewGPT - AI-Powered Interview Preparation System

## 📌 Project Description

InterviewGPT is an AI-powered interview preparation platform that helps users practice technical interviews through personalized question generation and intelligent answer evaluation. The application analyzes uploaded PDF resumes to extract technical skills and uses Retrieval-Augmented Generation (RAG) with Llama 3.1 to generate context-aware interview questions from uploaded knowledge documents.

The project is developed using Python, Streamlit, LangChain, Groq API, FAISS, and PyPDF.

---

# 📂 Project Structure

```
InterviewGPT/
│
├── app.py
├── evaluator.py
├── rag.py
├── resume_parser.py
├── skill_extractor.py
├── requirements.txt
├── README.md
```

---

# 🚀 Features

- AI-Powered Interview Preparation
- Resume PDF Upload and Analysis
- Automatic Skill Extraction
- Interview Questions PDF Upload
- RAG-Based Interview Question Generation
- AI-Powered Answer Evaluation
- Personalized Interview Feedback
- Interactive Streamlit Web Interface

---

# 🛠 Technologies Used

- Python
- Streamlit
- LangChain
- Groq API
- Llama 3.1
- FAISS
- PyPDF
- NLP

---

# 📄 Input Documents

The application accepts the following inputs:

- Resume PDF
- Interview Questions PDF

---

# ⚙️ Project Workflow

1. Upload Resume PDF
2. Extract Resume Text
3. Detect Technical Skills
4. Upload Interview Questions PDF
5. Create Vector Database using FAISS
6. Generate Interview Question using RAG
7. Enter Candidate Answer
8. AI-Based Answer Evaluation
9. Display Personalized Feedback

---

# ▶️ Running the Project

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Streamlit Application

```bash
streamlit run app.py
```

Open your browser and visit

```
http://localhost:8501
```

---

# 📷 Application Pages

- Home Page
- Resume Upload
- Resume Preview
- Detected Skills
- Interview Questions Upload
- Generated Interview Question
- Answer Evaluation
- AI Feedback Report

---

# 🧠 AI Components

### resume_parser.py

Extracts text from uploaded PDF resumes.

### skill_extractor.py

Identifies technical skills from the extracted resume text.

### rag.py

Creates a FAISS vector database and generates context-aware interview questions using Retrieval-Augmented Generation (RAG).

### evaluator.py

Evaluates candidate responses using the Groq API and Llama 3.1, providing personalized feedback on interview performance.

### app.py

Runs the Streamlit web application and integrates all project modules.

---

# 🎯 Future Enhancements

- Voice-Based Interview Practice
- Resume Score Prediction
- Download Evaluation Report as PDF
- User Authentication
- Interview History Tracking
- Multi-Language Support
- Performance Analytics Dashboard

---

# 👩‍💻 Developed By

**Gurram Sirisha**


# 📄 License

This project is developed for educational and learning purposes.


