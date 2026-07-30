import requests
import sys 
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent)) 
from config import OLLAMA_URL

class OllamaProvider:

    def __init__(self, model="llama3.2:latest"):
        self.model = model

    def generate(self, prompt: str):

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:

            response = requests.post(
                OLLAMA_URL,
                json=payload
            )

            response.raise_for_status()

            return response.json()["response"]

        except Exception as e:
            return f"Ollama Error : {e}"