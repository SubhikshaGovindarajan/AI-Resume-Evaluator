import streamlit as st
from PyPDF2 import PdfReader
from main import prompt

st.set_page_config(page_title="Resume_parser",layout="centered")
st.title("resume_parsing")
st.markdown('''
            upload your job description .
            paste your resume here.'''
            )
def extract_text(file):
    reader=PdfReader(file)
    text=""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

resume_text=st.text_area("paste your resume here",height=250)
jd_file=st.file_uploader("upload your jd here",type=["pdf","txt"])

jd_text=""
if jd_file:
    if jd_file.type=="application/pdf":
        jd_text=extract_text(jd_file)
    else:
        jd_text=jd_file.read().decode("utf-8")

if st.button("submit"):
    if not resume_text.strip() or not jd_text.strip():
        st.warning("invalid input")
    else:
        with st.spinner("loading"):
            try:
                response=prompt(resume_text,jd_text)
                st.subheader("your result")
                st.json(response)
            except Exception as e:
                st.error(e)
