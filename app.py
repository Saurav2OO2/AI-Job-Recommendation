import streamlit as st
from src.helper import extract_text_from_pdf, ask_ai
from src.job_api import fetch_linkedin_jobs, fetch_naukri_jobs

st.set_page_config(page_title='Job Recommender')
st.title('AI Job Recommender 🤖')
st.markdown('Upload your resume and get recomnedation based on your skills and experience from LinkedIn and Naukri')

upload_file = st.file_uploader('Uploader your resume (PDF)', type=['pdf'])

if upload_file:
    with st.spinner('Extracting text from your resume...'):
        resume_text = extract_text_from_pdf(upload_file)
    with st.spinner('Summarizing your resume...'):
        summary = ask_ai(f'Summarize this resume highlighting the skills,education and experience: {resume_text}', max_tokens=500)
    with st.spinner('Finding Skill Gaps...'):
        gaps = ask_ai(f'Analyze this resume and highlight missing skills, certifications & Experience needed for better job opportunity: {resume_text}', max_tokens=500)
    with st.spinner('Creating Future Roadmap...'):
        roadmap = ask_ai(f"Based on this resume suggest a future roadmap to improve this person's carrier prospects (Skills to learn, courses to take, Industry exposure) {resume_text}", max_tokens=500)

# Display nicely formatted results
    st.markdown("---")
    st.header("📑 Resume Summary")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{summary}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.header("🛠️ Skill Gaps & Missing Areas")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{gaps}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.header("🚀 Future Roadmap & Preparation Strategy")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{roadmap}</div>", unsafe_allow_html=True)

    st.success("✅ Analysis Completed Successfully!")

    if st.button('🔍 Get Job Recommendation'):
        with st.spinner('Fetching Job Recommendation...'):
            keywords = ask_ai(f'Based on this resume summary, suggest the best job titles and keywords for searching job. Give me a comma seaparated list only. no explaination \n\n, {summary}', max_tokens=100)

        search_keywords = keywords.replace('\n', '').strip()

        st.success(f'Extracted Job Keywords: {search_keywords}')

        with st.spinner('Fetching Job from LinkedIn and Naukri'):
            linkedin_jobs = fetch_linkedin_jobs(search_keywords, rows=60)
            naukri_jobs = fetch_naukri_jobs(search_keywords, rows=60)


    # Shows the Job on UI after fetching it from Linked in and Nuakri
        if linkedin_jobs:
            for job in linkedin_jobs:
                st.markdown(f"**{job.get('title')}** at *{job.get('companyName')}*")
                st.markdown(f"- 📍 {job.get('location')}")
                st.markdown(f"- 🔗 [View Job]({job.get('link')})")
                st.markdown("---")
        else:
            st.warning("No LinkedIn jobs found.")

        st.markdown("---")
        st.header("💼 Top Naukri Jobs (India)")

        if naukri_jobs:
            for job in naukri_jobs:
                st.markdown(f"**{job.get('title')}** at *{job.get('companyName')}*")
                st.markdown(f"- 📍 {job.get('location')}")
                st.markdown(f"- 🔗 [View Job]({job.get('url')})")
                st.markdown("---")
        else:
            st.warning("No Naukri jobs found.")