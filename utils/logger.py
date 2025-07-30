import streamlit as st

def init_logger():
    if "logs" not in st.session_state:
        st.session_state.logs = []

def log_message(msg):
    st.session_state.logs.append(msg)

def show_logger():
    st.sidebar.title("Logger")
    for log in st.session_state.logs:
        st.sidebar.write(log)