import os
from groq import Groq
from src.config import GROQ_MODEL, GROQ_API_KEY

client = Groq(
    api_key=GROQ_API_KEY,
)

def talk(query):
    prompt = f'''
    You are a friendly and concise chatbot. Keep your answers short (1–2 sentences), to the point, and warm. 
    After answering, gently ask a follow-up question to understand what the user needs or lead them toward their shopping goal.
    Avoid long explanations. Do not introduce yourself unless asked directly.
    
    QUESTION: {query}
    '''
    
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user", 
                "content": prompt
            }
        ],
        model=GROQ_MODEL,
    )
    
    return response.choices[0].message.content


if __name__ == "__main__":
    print(f"Q: How are you? ---> A: {talk('How are you?')}")
    print(f"Q: What is your name? ---> A: {talk('What is your name?')}")
    print(f"Q: Are you a robot? ---> A: {talk('Are you a robot?')}")
    print(f"Q: What do you do? ---> A: {talk('What do you do?')}")
    print(f"Q: What is your favorite color? ---> A: {talk('What is your favorite color?')}")