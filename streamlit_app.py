import streamlit as st
import cohere
import os
from dotenv import load_dotenv

# Only for local testing
if os.getenv("STREAMLIT_ENV") != "cloud":
    load_dotenv()

st.set_page_config(
    page_title="AI Q&A Bot",
    page_icon="✨",
    layout="centered"
)

# Get Cohere client
@st.cache_resource
def get_client():
    try:
        api_key = st.secrets["COHERE_API_KEY"]
        return cohere.Client(api_key)
    except KeyError:
        st.error("Missing COHERE_API_KEY in Streamlit Secrets!")
        st.stop()

client = get_client()

# Initialize chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

USER_AVATAR = "https://cdn-icons-png.flaticon.com/512/847/847969.png"
BOT_AVATAR = "https://cdn-icons-png.flaticon.com/512/4712/4712109.png"

st.title("AI Q&A Bot")
st.caption("Powered by Cohere + Streamlit")

# Render previous messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"""
            <div style="display:flex;justify-content:flex-end;margin:12px 0;">
                <div style="background:#2563eb;color:white;padding:12px 16px;border-radius:18px;max-width:75%;">
                    {msg['content']}
                </div>
                <img src="{USER_AVATAR}" style="width:38px;height:38px;border-radius:50%;margin-left:8px;">
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="display:flex;align-items:flex-start;margin:12px 0;">
                <img src="{BOT_AVATAR}" style="width:38px;height:38px;border-radius:50%;margin-right:8px;">
                <div style="background:#f3f4f6;color:#111827;padding:12px 16px;border-radius:18px;max-width:75%;">
                    {msg['content']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# User input
if prompt := st.chat_input("Type your question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.experimental_rerun()

# Process last user message
if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    last_prompt = st.session_state.messages[-1]["content"]
    try:
        with st.spinner("Thinking..."):
            response = client.chat(
                message=last_prompt,
                model="command-a-03-2025"
            )
            answer = response.text
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.experimental_rerun()
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=80)
    st.subheader("About")
    st.write("An AI-powered chatbot built with Cohere and Streamlit. Ask anything and get instant answers.")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.experimental_rerun()
