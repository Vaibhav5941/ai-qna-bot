import cohere
import os
from dotenv import load_dotenv

load_dotenv()

def initialize_cohere():
    api_key = os.getenv('COHERE_API_KEY')
    if not api_key:
        raise ValueError("COHERE_API_KEY not found in .env file")
    return cohere.Client(api_key)

def ask_question(client, question):
    try:
        response = client.chat(
            message=question,
            model='command-a-03-2025'
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("AI Q&A Bot")
    print("Type 'quit' or 'exit' to end\n")
    
    try:
        client = initialize_cohere()
        print("Connected to Cohere\n")
    except Exception as e:
        print(f"Failed to initialize: {e}")
        return
    
    while True:
        question = input("You: ").strip()
        
        if question.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break
        
        if not question:
            print("Please ask a question!\n")
            continue
        
        answer = ask_question(client, question)
        print(f"Bot: {answer}\n")

if __name__ == "__main__":
    main()
