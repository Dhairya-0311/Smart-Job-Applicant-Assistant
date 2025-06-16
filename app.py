import streamlit as st
from resume_utils import extract_text_from_pdf, extract_text_from_docx
from ai_utils import generate_cover_letter, generate_resume_summary, calculate_ats_score

st.set_page_config(page_title="Smart Job Application Assistant", page_icon="🧠", layout="wide")
st.title("🧠 Smart Job Application Assistant")

st.markdown("Easily generate a tailored cover letter and resume summary with AI—and check your ATS match score!")

job_desc = st.text_area("📌 Paste the Job Description", height=200)
resume = st.file_uploader("📄 Upload Your Resume (PDF or DOCX)", type=["pdf", "docx"])

resume_text = ""
if resume:
    with st.spinner("📂 Extracting resume text..."):
        if resume.name.endswith(".pdf"):
            resume_text = extract_text_from_pdf(resume)
        elif resume.name.endswith(".docx"):
            resume_text = extract_text_from_docx(resume)
        else:
            st.error("Unsupported file type. Please upload a PDF or DOCX.")

# Button layout using columns
if job_desc and resume_text:
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("✍ Generate Cover Letter"):
            with st.spinner("Generating cover letter..."):
                cover_letter = generate_cover_letter(job_desc, resume_text)
                st.subheader("📄 AI-Crafted Cover Letter")
                st.write(cover_letter)

    with col2:
        if st.button("📝 Resume Summary"):
            with st.spinner("Generating summary..."):
                summary = generate_resume_summary(resume_text, job_desc)
                st.subheader("📌 Tailored Resume Summary")
                st.write(summary)

    with col3:
        if st.button("📊 ATS Match Score"):
            with st.spinner("Calculating match score..."):
                score = calculate_ats_score(resume_text, job_desc)
                st.metric(label="🔍 ATS Match Score", value=f"{score}%", delta=None)
                st.info("Score is based on keyword similarity between your resume and the job description.")