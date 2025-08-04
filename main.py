import sys
from pathlib import Path
import streamlit as st
from src.router import router
from src.chains import faq, smalltalk, sql
from src.config import FAQ_PATH

# Ensure root is in sys.path if needed
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Load FAQ data once
@st.cache_resource
def load_faq():
    faq.ingest_faq_data(FAQ_PATH)
    return True

load_faq()

def ask(query):
    route = router(query)
    if route.name == "faq":
        return faq.faq_chain(query)
    elif route.name == "smalltalk":
        return smalltalk.talk(query)
    elif route.name == "sql":
        return sql.sql_chain(query)
    return "🤖 Sorry, I don't understand your question."

# --- UI ---

st.set_page_config(page_title="E-commerce Chatbot", page_icon="🛍️", layout="centered")
st.markdown("<h1 style='text-align: center;'>🛍️ E-commerce Chatbot Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ask me anything about our products, policies, or support!</p>", unsafe_allow_html=True)
st.divider()

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat Input (new Streamlit feature)
query = st.chat_input("Type your question here...")

if query:
    st.chat_message("user").markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})

    with st.spinner("Thinking..."):
        response = ask(query)

    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
