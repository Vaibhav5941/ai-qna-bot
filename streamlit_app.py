import streamlit as st
import cohere
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Q&A Bot",
    page_icon="🤖",
    layout="centered"
)

# Initialize Cohere
@st.cache_resource
def get_cohere_client():
    api_key = os.getenv('COHERE_API_KEY')
    if not api_key:
        st.error("COHERE_API_KEY not found in .env file")
        st.stop()
    return cohere.Client(api_key)

# Main app
st.title("🤖 AI Q&A Bot")
st.markdown("*Powered by Cohere AI*")
st.divider()

# Initialize client
client = get_cohere_client()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat(
                    message=prompt,
                    model='command-a-03-2025'
                )
                answer = response.text
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Sidebar
with st.sidebar:
    st.header("About")
    st.info("This is a simple AI Q&A bot built with Cohere and Streamlit.")
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()