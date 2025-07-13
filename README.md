# Resume-Analyser_
# 📄 AI Resume Analyzer and Job Matcher

A Streamlit web application that analyzes resumes and matches skills to popular job roles using simple text extraction and keyword-based logic.

## 🔍 Project Overview

This tool helps students and job seekers get feedback on how well their resumes align with key industry roles such as:

- Data Scientist
- Web Developer
- Software Engineer
- AI/ML Engineer
- Business Analyst

It extracts skill-related keywords from a PDF resume and calculates a match score against predefined job roles, highlighting missing skills and areas for improvement.

## 🛠 Features

- 📤 Upload PDF resume directly
- 📑 Extract raw text from resume using `pdfplumber`
- 🔍 Identify technical and soft skills
- 📊 Calculate match scores for various job profiles
- ⚠️ Show missing skills to help improve resume fit
- 🧪 Includes debug mode to show raw extracted text

## 🚀 Tech Stack

- **Python**
- **Streamlit** – frontend web interface
- **pdfplumber** – for text extraction from resumes
- **Set logic** – for skill matching and scoring

## 📂 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/resume-analyzer.git
   cd resume-analyzer

