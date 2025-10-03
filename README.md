What Worked ✅

Setting up Python and pip
Creating GitHub repository
Using Cohere API (great documentation!)
Building command-line interface
Adding Streamlit UI (surprisingly easy!)

Challenges I Faced 🤔

API Key Security: Initially didn't know about .env files

Solution: Googled "how to hide API keys python" → Found python-dotenv


Cohere API: First time using it

Solution: Read Cohere docs, tried different models


Streamlit Chat Interface: Wanted persistent chat history

Solution: Used st.session_state after checking Streamlit docs



Resources I Used 📚

Python Official Docs
Cohere Documentation
Streamlit Documentation
Render Deployment Guide
Stack Overflow for debugging
ChatGPT/Claude for code examples

Time Spent ⏱️

Setup & Learning: 1 hour
Command-line bot: 45 minutes
Streamlit UI: 1 hour
Documentation: 30 minutes
Total: ~3 hours


How to Use This Repository

Clone the repo

bash   git clone https://github.com/YOUR_USERNAME/ai-qna-bot.git
   cd ai-qna-bot

Install dependencies

bash   pip install -r requirements.txt

Add your API key

Create .env file
Add: COHERE_API_KEY=your_key_here


Run the app

Command-line: python app.py
Streamlit UI: streamlit run streamlit_app.py




Next Steps / Future Improvements

 Add conversation history saving
 Support different AI models
 Add rate limiting
 Improve error handling
 Add unit tests
 Create Docker container


License
MIT License - Feel free to use and modify!
Contact
Questions? Open an issue on GitHub!