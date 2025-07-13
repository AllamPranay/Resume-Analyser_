# app.py
import streamlit as st
import pdfplumber

# Extended skill keywords for better matching
SKILL_KEYWORDS = [
    "python", "java", "c++", "c plus plus", "sql", "r", "excel",
    "machine learning", "ml", "deep learning", "data analysis", "data science",
    "statistics", "communication", "problem solving", "teamwork", "leadership",
    "html", "css", "javascript", "react", "django", "flask", "pandas", "numpy", "matplotlib", "scikit-learn"
]

# Predefined job roles with expected skills
JOB_ROLES = [
    {
        "role": "Data Scientist",
        "skills": ["python", "machine learning", "data analysis", "sql", "pandas", "scikit-learn", "statistics"]
    },
    {
        "role": "Web Developer",
        "skills": ["html", "css", "javascript", "python", "flask", "django", "react"]
    },
    {
        "role": "Software Engineer",
        "skills": ["java", "c++", "problem solving", "communication", "python"]
    },
    {
        "role": "AI/ML Engineer",
        "skills": ["python", "deep learning", "machine learning", "numpy", "pandas", "scikit-learn"]
    },
    {
        "role": "Business Analyst",
        "skills": ["excel", "sql", "data analysis", "communication", "python"]
    }
]

# Extract text from PDF using pdfplumber
@st.cache_data
def extract_text_from_resume(file):
    text = ""
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
    return text.lower()

# Match skill keywords inside the extracted text
def extract_skills(text):
    found_skills = set()
    for skill in SKILL_KEYWORDS:
        if skill.lower() in text:
            found_skills.add(skill.lower())
    return list(found_skills)

# Calculate how well the resume matches each job role
def match_resume_to_jobs(resume_skills):
    results = []
    for job in JOB_ROLES:
        required = set(job["skills"])
        matched = required.intersection(resume_skills)
        missing = required - matched
        score = int((len(matched) / len(required)) * 100) if required else 0
        results.append({
            "role": job["role"],
            "score": score,
            "missing_skills": sorted(list(missing))
        })
    return results

# Streamlit interface
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("📄 AI Resume Analyzer and Job Matcher")

st.write("""
Upload your resume (PDF), and this app will extract the text and analyze your skills.
It will compare your skills with industry job roles and suggest how well you match,
along with missing skills.
""")

uploaded_file = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])

if uploaded_file:
    with st.spinner("Analyzing your resume..."):
        text = extract_text_from_resume(uploaded_file)
        resume_skills = extract_skills(text)
        match_results = match_resume_to_jobs(resume_skills)

    st.success("✅ Analysis Complete!")

    st.subheader("🔍 Extracted Skills")
    st.write(", ".join(resume_skills) if resume_skills else "No skills detected. Try a different resume format.")

    st.subheader("📊 Job Match Scores")
    for job in match_results:
        st.markdown(f"**{job['role']}** — ✅ Match Score: {job['score']}%")
        if job['missing_skills']:
            st.markdown(f"⚠️ Missing Skills: {', '.join(job['missing_skills'])}")
        st.markdown("---")

    # Show raw extracted text for debugging
    st.subheader("📄 Extracted Resume Text (Debug Mode)")
    st.text_area("Resume Text:", value=text[:3000], height=250)
else:
    st.warning("📤 Please upload a PDF resume to begin analysis.")
