import streamlit as st
from interviewer import get_interview_question
from pypdf import PdfReader
import io
import json
from datetime import datetime


def save_interview(topic, level, messages):
    history = []
    try:
        with open("history.json", "r") as f:
            history = json.load(f)
    except:
        history = []
    
    history.append({
        "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "topic": topic,
        "level": level,
        "messages": messages
    })
    
    with open("history.json", "w") as f:
        json.dump(history, f, indent=2)


st.title(" AI Interview Coach")
st.subheader("Practice your interview skills with AI")

with st.sidebar:
    st.header(" Settings")
    
    topic_option = st.selectbox(
        "Interview Topic",
        ["AI/ML", "Python", "Data Science", "HR", "Custom..."]
    )

    if topic_option == "Custom...":
        topic = st.text_input("Enter your topic:")
    else:
        topic = topic_option
    
    level = st.selectbox(
        "Your Level",
        ["Junior", "Mid-level", "Senior"]
    )

    st.divider()
    uploaded_file = st.file_uploader("📄 Upload PDF (optional)", type="pdf")
    
    pdf_text = ""
    if uploaded_file:
        reader = PdfReader(io.BytesIO(uploaded_file.read()))
        for page in reader.pages:
            pdf_text += page.extract_text()
        st.success("PDF loaded! ✅")
    
    if st.button(" Start New Interview"):
        st.session_state.messages = []
        st.session_state.started = True

    if st.session_state.get("started"):
        if st.button(" End & Save Interview"):
            save_interview(topic, level, st.session_state.messages)
            st.session_state.started = False
            st.session_state.messages = []
            st.success("Interview saved! ✅")
            st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "started" not in st.session_state:
    st.session_state.started = False

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if st.session_state.started:
    user_input = st.chat_input("Your answer here...")
    
    if user_input:
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })
        
        ai_response = get_interview_question(
            topic, 
            level, 
            st.session_state.messages,
            pdf_text
        )
        
        st.session_state.messages.append({
            "role": "assistant",
            "content": ai_response
        })
        
        st.rerun()