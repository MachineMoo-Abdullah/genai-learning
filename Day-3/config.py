import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("Groq_API_Key") or os.getenv("GROQ_API_KEY")

GROQ_BASE_URL = "https://api.groq.com/openai/v1"