from pathlib import Path
import pandas 
import chromadb
from chromadb.utils import embedding_functions
from groq import Groq
from src.config import GROQ_MODEL, GROQ_API_KEY, EMBEDDING_MODEL

ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL
    )

chroma_client = chromadb.Client()
groq_client = Groq(api_key=GROQ_API_KEY)
collection_name_faq = 'faqs'

def ingest_faq_data(path):
    if collection_name_faq not in [c.name for c in chroma_client.list_collections()]:
        print("Ingesting FAQ data into Chromadb...")
        collection = chroma_client.create_collection(
            name=collection_name_faq,
            embedding_function=ef
        )
        df = pandas.read_csv(path)
        docs = df['question'].to_list()
        metadata = [{'answer': ans} for ans in df['answer'].to_list()]
        ids = [f"id_{i}" for i in range(len(docs))]
        collection.add(
            documents=docs,
            metadatas=metadata,
            ids=ids
        )
        print(f"FAQ Data successfully ingested into Chroma collection: {collection_name_faq}")
    else:
        print(f"Collection: {collection_name_faq} already exists")

def get_relevant_qa(query):
    collection = chroma_client.get_collection(
        name=collection_name_faq,
        embedding_function=ef
    )
    result = collection.query(
        query_texts=[query],
        n_results=2
    )

    return result

def generate_answer(query, context):
    prompt = f'''
    You are a customer support assistant for an e-commerce platform. 
    Use ONLY the provided context to answer the customer query. 

    Instructions:
    - Answer briefly, clearly, and professionally.
    - If the context does NOT contain the answer, respond with: "I'm not sure about that. Let me connect you to a support agent."
    - Do NOT make up answers or use outside knowledge.
    - Keep it under 2-3 sentences.
    
    CONTEXT: {context}
    
    QUESTION: {query}
    '''

    response = groq_client.chat.completions.create(
        messages=[
            {
                "role": "user", 
                "content": prompt
            }
        ],
        model=GROQ_MODEL,
    )
    
    return response.choices[0].message.content

def faq_chain(query):
    result = get_relevant_qa(query)
    if not result['metadatas'][0]:
        return "I don't know"
    
    context = "".join([r.get('answer') for r in result['metadatas'][0]])
    answer = generate_answer(query, context)
    
    return answer


if __name__ == '__main__':
    ingest_faq_data("data/faq_data.csv")

    test_questions = [
        "what's your policy on defective products?",
        "Do you take cash as a payment option?",
        "What is the revenue of flipkart?"
    ]

    for question in test_questions:
        answer = faq_chain(question)
        print(f"Q: {question} ---> A: {answer}")