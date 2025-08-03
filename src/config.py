import os
from dotenv import load_dotenv

load_dotenv()

# Sensitive data from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Other constants
GROQ_MODEL="llama-3.3-70b-versatile"
EMBEDDING_MODEL="sentence-transformers/all-MiniLM-L6-v2"
TEMPARATURE=0.2
MAX_TOKENS=1024
DB_PATH = "src/database/db.sqlite"
