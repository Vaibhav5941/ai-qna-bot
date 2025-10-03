import cohere
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def initialize_cohere():
    """Initialize Cohere client with API key"""
    api_key = os.getenv('COHERE_API_KEY')
    if not api_key:
        raise ValueError("COHERE_API_KEY not found in .env file")
    return cohere.Client(api_key)

def ask_question(client, question):
    """Send question to Cohere and get response"""
    try:
        response = client.chat(
            message=question,
            model='command-a-03-2025'
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """Main application loop"""
    print("=" * 50)
    print("🤖 AI Q&A Bot (Powered by Cohere)")
    print("=" * 50)
    print("Type 'quit' or 'exit' to end the conversation\n")
    
    # Initialize Cohere
    try:
        client = initialize_cohere()
        print("✅ Connected to Cohere API\n")
    except Exception as e:
        print(f"❌ Failed to initialize: {e}")
        return
    
    # Chat loop
    while True:
        question = input("You: ").strip()
        
        if question.lower() in ['quit', 'exit', 'bye']:
            print("\n👋 Goodbye! Thanks for chatting!")
            break
        
        if not question:
            print("⚠️  Please ask a question!\n")
            continue
        
        print("\n🤔 Thinking...\n")
        answer = ask_question(client, question)
        print(f"Bot: {answer}\n")
        print("-" * 50 + "\n")

if __name__ == "__main__":
    main()