from google import genai
import sys 
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent)) 
from config import GEMINI_API_KEY

class GeminiProvider:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = "gemini-3.5-flash"

    def generate(self, prompt: str):

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )

            return response.text

        except Exception as e:
            return f"Gemini Error : {e}"

