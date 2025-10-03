⚡ Quick Start Guide
Get your AI Q&A Bot running in 5 minutes!
🎯 Prerequisites Checklist
Before you start, make sure you have:

 Python 3.8+ installed (Download here)
 Git installed (Download here)
 A Cohere account (Sign up free)
 A GitHub account (Sign up free)
 A text editor (VS Code, Notepad++, etc.)


🚀 5-Minute Setup
Step 1: Get Your Cohere API Key (2 minutes)

Go to cohere.com and sign up
Click on your profile → API Keys
Copy your Trial Key (it's free!)
Save it somewhere safe (you'll need it in Step 4)

Step 2: Create GitHub Repository (1 minute)

Go to github.com/new
Repository name: ai-qna-bot
✅ Check "Add a README file"
Click Create repository
Click the green Code button and copy the URL

Step 3: Download and Setup (1 minute)
Option A: Clone the template
bash# If you're using a template repository:
git clone YOUR_GITHUB_URL
cd ai-qna-bot
Option B: Start from scratch
bash# Create project folder
mkdir ai-qna-bot
cd ai-qna-bot

# Initialize git
git init
git remote add origin YOUR_GITHUB_URL
Step 4: Install Dependencies (30 seconds)
Create requirements.txt:
textcohere
python-dotenv
streamlit
Install:
bashpip install -r requirements.txt
Step 5: Add Your API Key (30 seconds)
Create .env file:
bash# Mac/Linux:
touch .env

# Windows:
echo. > .env
Edit .env and add:
COHERE_API_KEY=paste_your_key_here
⚠️ IMPORTANT: Create .gitignore to protect your key:
.env
__pycache__/
*.pyc
venv/
Step 6: Run the Bot! (30 seconds)
Command-line version:
bashpython app.py
Web interface:
bashstreamlit run streamlit_app.py

📝 File Structure
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
└── deploy.sh             # Deployment helper

🎨 Usage Examples
Command-Line Bot
bash$ python app.py

🤖 AI Q&A Bot (Powered by Cohere)
==================================================
Type 'quit' or 'exit' to end the conversation

✅ Connected to Cohere API

You: What is Python?

🤔 Thinking...

Bot: Python is a high-level, interpreted programming language...

You: quit

👋 Goodbye! Thanks for chatting!
Web Interface
bash$ streamlit run streamlit_app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
Then open your browser and chat away! 💬

🔍 Common Issues & Quick Fixes
Issue: "python: command not found"
Fix: Try python3 instead:
bashpython3 app.py
Issue: "COHERE_API_KEY not found"
Fix: Make sure .env file is in the same folder as your Python files.
Issue: "Module not found"
Fix: Install requirements:
bashpip install -r requirements.txt
Issue: Port already in use (Streamlit)
Fix: Use a different port:
bashstreamlit run streamlit_app.py --server.port 8502
For more help, see TROUBLESHOOTING.md

🚀 Deploy to Render (5 minutes)
1. Push to GitHub
bashgit add .
git commit -m "Initial commit"
git push -u origin main
2. Deploy on Render

Go to render.com and sign up
Click New + → Web Service
Connect your GitHub repository
Configure:

Build Command: pip install -r requirements.txt
Start Command: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0


Add Environment Variable:

Key: COHERE_API_KEY
Value: Your Cohere API key


Click Create Web Service
Wait 2-3 minutes ⏱️

Done! Your app is live at https://your-app.onrender.com 🎉

💡 Pro Tips
Tip 1: Use Virtual Environments
Keeps your project isolated:
bash# Create virtual environment
python -m venv venv

# Activate it
# Mac/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
Tip 2: Save Your Chat History
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
Try different Cohere models for speed vs quality:
python# Fast and efficient
model='command'

# More powerful
model='command-r-plus'

# Balanced
model='command-r'
Tip 4: Add Rate Limiting
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

📚 Next Steps
Once you have the basic bot running:

✅ Customize the UI - Change colors, add your logo
✅ Add features - File upload, voice input, export chat
✅ Improve responses - Add system prompts, context
✅ Add analytics - Track usage, popular questions
✅ Create tests - Ensure everything works
✅ Write documentation - Help others understand your code


🆘 Need Help?

📖 Read TROUBLESHOOTING.md
🐛 Check GitHub Issues
💬 Ask in Cohere Discord
📧 Contact: your.email@example.com


🎓 Learning Resources

Cohere Documentation
Streamlit Tutorial
Python Dotenv Guide
Git Basics


Happy Coding! 🚀
Remember: Everyone starts somewhere. If you get stuck, don't give up - debugging is part of learning!