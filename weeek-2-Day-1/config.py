import os
from dotenv import load_dotenv

load_dotenv()

# Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# OpenRouter
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"
