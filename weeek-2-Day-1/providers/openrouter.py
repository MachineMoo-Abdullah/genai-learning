import requests
import sys 
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent)) 
from config import OPENROUTER_API_KEY


class OpenRouterProvider:

    def __init__(self,
                 model="deepseek/deepseek-chat-v3-0324"):

        self.model = model

    def generate(self, prompt: str):

        if not OPENROUTER_API_KEY:
            return "OpenRouter API Key not found."

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {

            "model": self.model,

            "messages": [

                {
                    "role": "user",
                    "content": prompt
                }

            ]

        }

        try:

            response = requests.post(

                "https://openrouter.ai/api/v1/chat/completions",

                headers=headers,

                json=payload,

                timeout=120

            )

            response.raise_for_status()

            return response.json()["choices"][0]["message"]["content"]

        except Exception as e:

            return f"OpenRouter Error : {e}"