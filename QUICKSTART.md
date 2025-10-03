Quick Start Guide
=================
Get your AI Q&A Bot running in 5 minutes!

1. Prerequisites Checklist
   Before you start, make sure you have:

 # Python 3.8+ installed (Download here)
 # Git installed (Download here)
 # A Cohere account (Sign up free)
 # A GitHub account (Sign up free)
 # A text editor (VS Code, Notepad++, etc.)

2. 5-Minute Setup
 Step 1: Get Your Cohere API Key (2 minutes)
 # Go to cohere.com and sign up
 # Click on your profile → API Keys
 # Copy your Trial Key (it's free!)
 # Save it somewhere safe (you'll need it in Step 4)

 Step 2: Create GitHub Repository (1 minute)
 # Go to github.com/new
 # Repository name: ai-qna-bot
 # ✅ Check "Add a README file"
 # Click Create repository
 # Click the green Code button and copy the URL

 Step 3: Download and Setup (1 minute)
 # Option A: Clone the template
    bash# If you're using a template repository:
    git clone https://github.com/Vaibhav5941/ai-qna-bot.git
    cd ai-qna-bot

 # Option B: Start from scratch
    bash# Create project folder
    mkdir ai-qna-bot
    cd ai-qna-bot
 # Initialize git
    git init
    git remote https://github.com/Vaibhav5941/ai-qna-bot.git


 Step 4: Install Dependencies (30 seconds)
 # Create requirements.txt:
   textcohere
   python-dotenv
   streamlit
 # Install:
   bashpip install -r requirements.txt

 Step 5: Add Your API Key (30 seconds)
   Create .env file:
  # Mac/Linux:
   touch .env

  # Windows:
   echo. > .env

Edit .env and add:
 COHERE_API_KEY=paste_your_key_here

IMPORTANT: Create .gitignore to protect your key:
 .env
 __pycache__/
 *.pyc
 venv/

Step 6: Run the Bot! (30 seconds)
 # Command-line version:
   python app.py
 # Web interface:
   streamlit run streamlit_app.py

File Structure
Your project should look like this:
ai-qna-bot/
│
├── app.py                 # Command-line bot
├── streamlit_app.py       # Web interface
├── requirements.txt       # Dependencies
├── .env                   # Your API key (SECRET!)
├── .gitignore            # Protect secrets
├── README.md             # Project documentation
├── TROUBLESHOOTING.md    # Help with issues
└── QUICKSTART.md         # 5-Minute Setup Guide

Usage Examples:
==============
Command-Line Bot

bash$ python app.py

AI Q&A Bot (Powered by Cohere)
==================================================
Type 'quit' or 'exit' to end the conversation

Connected to Cohere API

You: What is Python?

Thinking...

Bot: Python is a high-level, interpreted programming language...

You: quit

Goodbye! Thanks for chatting!

Web Interface:
=============
 streamlit run streamlit_app.py
 You can now view your Streamlit app in your browser.
 Local URL: http://localhost:8501

Then open your browser and chat away! 💬

Common Issues & Quick Fixes:
===========================

Issue: "python: command not found"
Fix: Try python3 instead:
   python3 app.py

Issue: "COHERE_API_KEY not found"
Fix: Make sure .env file is in the same folder as your Python files.

Issue: "Module not found"
Fix: Install requirements:
   pip install -r requirements.txt

Issue: Port already in use (Streamlit)
Fix: Use a different port:
   streamlit run streamlit_app.py --server.port 8502

For more help, see TROUBLESHOOTING.md

Deploy to streamlit community cloud (5 minutes):
===============================================
1. Prepare your project folder
Your folder should contain:

ai-qna-bot/
│
├── app.py                 # Command-line bot
├── streamlit_app.py       # Web interface
├── requirements.txt       # Dependencies
├── .env                   # Your API key (SECRET!)

2. Create requirements.txt
 Streamlit Cloud needs a requirements.txt to install dependencies. For your app:

 streamlit
 cohere
 python-dotenv

3. Change your get_client() function to:

@st.cache_resource
def get_client():
    api_key = st.secrets["COHERE_API_KEY"]
    if not api_key:
        st.error("Missing COHERE_API_KEY in Streamlit Secrets")
        st.stop()
    return cohere.Client(api_key)

You can now ignore the .env file, Streamlit will inject the secret safely.

4. Push to GitHub
git add .
git commit -m "Initial commit"
git push -u origin main

5. Deploy on streamlit community cloud

 Go to Streamlit Cloud
 Click "New App" → "Deploy from GitHub repo". 
 Select your repository and branch (main).
 Streamlit will automatically detect app.py and requirements.txt.
 Click "Deploy".

Your bot should now run online!

Click Create Web Service
Wait 2-3 minutes 

Done! Your app is live at https://ai-qna-bot.streamlit.app/ 

💡 Pro Tips
Tip 1: Use Virtual Environments
===============================
Keeps your project isolated:
 Create virtual environment
 python -m venv venv

# Activate it
# Mac/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

Tip 2: Save Your Chat History
=============================
Add this to streamlit_app.py:
pythonimport json

# Save chat
def save_chat():
    with open('chat_history.json', 'w') as f:
        json.dump(st.session_state.messages, f)

# Add a save button
if st.button("Save Chat"):
    save_chat()
    st.success("Chat saved!")

Tip 3: Use Different Models
===========================
Try different Cohere models for speed vs quality:
python# Fast and efficient
model='command'

# More powerful
model='command-r-plus'

# Balanced
model='command-r'

Tip 4: Add Rate Limiting
========================
Prevent hitting API limits:
pythonimport time

last_request = 0

def rate_limited_ask(question):
    global last_request
    
    # Wait at least 1 second between requests
    elapsed = time.time() - last_request
    if elapsed < 1:
        time.sleep(1 - elapsed)
    
    response = client.chat(message=question, model='command-r-plus')
    last_request = time.time()
    
    return response.text


🆘 Need Help?

📖 Read TROUBLESHOOTING.md
🐛 Check GitHub Issues
💬 Ask in Cohere Discord
📧 Contact: gvaibhav5941@gmail.com


🎓 Learning Resources

Cohere Documentation
Streamlit Tutorial
Python Dotenv Guide
Git Basics


Happy Coding! 🚀
Remember: Everyone starts somewhere. If you get stuck, don't give up - debugging is part of learning!