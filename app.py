import streamlit as st
from gemini_utils import classify_threat, detect_phishing, summarize_incident
from phishing_examples import examples

st.set_page_config(page_title="AI-CERT", layout="wide")
st.title("🛡️ AI-CERT: Cyber Threat Assistant")

st.markdown("Enter any email, log, or message related to a cyber incident:")

input_text = st.text_area("Paste cyber message here:", height=200)

col1, col2, col3 = st.columns(3)

if st.button("🕵️‍♀️ Analyze Now"):
    with col1:
        st.markdown("### 🔍 Threat Type")
        st.info(classify_threat(input_text))

    with col2:
        st.markdown("### ⚠️ Phishing Detection")
        st.warning(detect_phishing(input_text))

    with col3:
        st.markdown("### 📄 Summary")
        st.success(summarize_incident(input_text))

st.sidebar.markdown("### 💡 Try Sample Emails")
for i, sample in enumerate(examples):
    if st.sidebar.button(f"Example {i+1}"):
        st.session_state['text'] = sample
        st.experimental_rerun()
