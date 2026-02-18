# AI Job Application Assistant 🤖📄

## Overview
The **AI Job Application Assistant** is a LangChain-based mini project that helps candidates tailor their job applications using Generative AI.  
It dynamically analyzes a job description, evaluates a candidate’s resume, suggests improvements, and generates a professional cover letter.

The project is **role-agnostic**, meaning it works for **any job role** (e.g., Machine Learning Intern, Software Engineer, Data Analyst, etc.).

---

## Features

### 1️⃣ Job Description Analyzer
- Extracts structured job requirements from unstructured text
- Uses **Pydantic + PydanticOutputParser**
- Extracts:
  - Job title
  - Required skills
  - Experience required
  - Tools
  - Soft skills

### 2️⃣ Resume Improvement Suggestions
- Compares resume against job requirements
- Identifies missing skills
- Suggests actionable improvements
- Provides an overall fit summary
- Uses **PydanticOutputParser** for validated output

### 3️⃣ Cover Letter Generator
- Generates a professional, role-specific cover letter
- Uses **StrOutputParser**
- Output is plain text (no JSON)

---

## Tech Stack
- Python 3.12
- LangChain Core
- Google Gemini 2.5 Flash (Free Tier)
- Pydantic

---

## Project Structure

```text
ai_job_application_assistant/
│
├── job_analyzer.py
├── resume_suggester.py
├── cover_letter_generator.py
├── main.py
├── requirements.txt
└── README.md
