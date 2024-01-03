import streamlit as st

def init_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "crawl_content" not in st.session_state:
        st.session_state.crawl_content = ""

    if "crawl_summary" not in st.session_state:
        st.session_state.crawl_summary = ""