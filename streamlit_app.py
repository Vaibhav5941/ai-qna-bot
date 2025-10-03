import streamlit as st
import cohere
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="AI Q&A Bot",
    page_icon="✨",
    layout="centered"
)

@st.cache_resource
def get_client():
    api_key = os.getenv('COHERE_API_KEY')
    if not api_key:
        st.error("Missing COHERE_API_KEY in .env file")
        st.stop()
    return cohere.Client(api_key)

st.markdown(
    """
    <style>
        
        .stApp {
        background: ;
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        }
        
        .chat-row {
            display: flex;
            align-items: flex-start;
            margin: 12px 0;
        }
        .chat-bubble {
            padding: 12px 16px;
            border-radius: 18px;
            max-width: 75%;
            line-height: 1.5;
            font-size: 16px;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.05);
            word-wrap: break-word;
        }
        .user-msg {
            background-color: #2563eb;
            color: white;
            margin-left: auto;
            border-bottom-right-radius: 6px;
            animation: fadeInRight 0.3s ease;
        }
        .bot-msg {
            background-color: #f3f4f6;
            color: #111827;
            margin-right: auto;
            border-bottom-left-radius: 6px;
            animation: fadeInLeft 0.3s ease;
        }
        .avatar {
            width: 38px;
            height: 38px;
            border-radius: 50%;
            margin: 0 8px;
            object-fit: cover;
        }
        @keyframes fadeInRight {
            from {opacity: 0; transform: translateX(30px);}
            to {opacity: 1; transform: translateX(0);}
        }
        @keyframes fadeInLeft {
            from {opacity: 0; transform: translateX(-30px);}
            to {opacity: 1; transform: translateX(0);}
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("AI Q&A Bot")
st.caption("Powered by Cohere + Streamlit")

client = get_client()

if "messages" not in st.session_state:
    st.session_state.messages = []


USER_AVATAR = "https://cdn-icons-png.flaticon.com/512/847/847969.png"
BOT_AVATAR = "https://cdn-icons-png.flaticon.com/512/4712/4712109.png"

# Render chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"""
            <div class="chat-row" style="justify-content: flex-end;">
                <div class="chat-bubble user-msg">{msg['content']}</div>
                <img src="{USER_AVATAR}" class="avatar">
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class="chat-row">
                <img src="{BOT_AVATAR}" class="avatar">
                <div class="chat-bubble bot-msg">{msg['content']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# User input
if prompt := st.chat_input("Type your question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(
        f"""
        <div class="chat-row" style="justify-content: flex-end;">
            <div class="chat-bubble user-msg">{prompt}</div>
            <img src="{USER_AVATAR}" class="avatar">
        </div>
        """,
        unsafe_allow_html=True
    )
    try:
        with st.spinner("Thinking..."):
            response = client.chat(
                message=prompt,
                model="command-a-03-2025"
            )
            answer = response.text
            # Store bot reply (Markdown supported in Streamlit)
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.markdown(
                f"""
                <div class="chat-row">
                    <img src="{BOT_AVATAR}" class="avatar">
                    <div class="chat-bubble bot-msg">{answer}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=80)
    st.subheader("About")
    st.write("An AI-powered chatbot built with Cohere and Streamlit. Ask anything and get instant answers.")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
