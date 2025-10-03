AI Q&A Bot

Ever wondered what it feels like to chat with an AI that actually gets your questions? I built this AI Q&A Bot to explore exactly that—using Python, the Cohere API, and Streamlit. Along the way, I learned a ton, faced a few hurdles, and ended up with a working bot that’s surprisingly fun to interact with.

My Journey 
==========

What Worked:
    1.Setting up Python and pip was straightforward.
    2.Creating a GitHub repo helped me track everything neatly.
    3.The Cohere API was surprisingly intuitive—once I got the hang of it.
    4.Building a command-line interface gave me a quick proof of concept.
    5.Adding a Streamlit UI made the bot accessible to anyone with a browser!

The Hurdles I Hit:
=================

   1. Hiding API Keys: At first, I had no clue how to keep my API key secure. A quick search led me to .env files with python-dotenv. Problem solved!

   2. Cohere API First Use: Experimenting with models was tricky. I ended up reading the docs thoroughly and testing different options until it clicked.

   3. Persistent Chat in Streamlit: I wanted the chat to remember the conversation. st.session_state saved the day.

Resources That Saved Me:
=======================

   1. Python Official Docs
   2. Cohere API Documentation
   3. Streamlit Documentation
   4. streamlit community cloud Deployment Guides
   5. Stack Overflow for debugging
   6. ChatGPT & Claude for code examples

Time Breakdown:
==============
       Task                                      	Time Spent

    1. Setup & Learning	                            1 hour 
    2. Command-line bot	                            45 minutes
    3. Streamlit UI	                                1 hour
    4. Writing Documentation	                    30 minutes
    ----------------------------------------------------------
        Total                                    	~3 hours

How to Try It Yourself:
======================

1. Clone the repo:

git clone https://github.com/Vaibhav5941/ai-qna-bot.git
cd ai-qna-bot

2. Install dependencies:

pip install -r requirements.txt


3. Add your Cohere API key:

  a. Create a .env file in the project root
  b. Add your key:
     COHERE_API_KEY=your_key_here

4. Run the bot:

   a. Command-line interface:
    python app.py

   b. Streamlit web UI:
    streamlit run streamlit_app.py

Next Steps ✨
==========
This project is just the beginning. Future improvements I’d love to add:
1. Save conversation history to revisit chats later
2. Support multiple AI models for more variety
3. Rate limiting for smooth performance
4. Better error handling
5. Unit tests to ensure reliability
6. streamlit community cloud for simple deployment 


Got Questions? 
Open an issue on GitHub—I’d love to hear your thoughts, suggestions, or even just say hi!