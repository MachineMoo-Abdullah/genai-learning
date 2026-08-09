import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()


class LLMService:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise RuntimeError(
                "GEMINI_API_KEY is missing. "
                "Add it to your .env file."
            )

        self.model = os.getenv(
            "GEMINI_MODEL",
            "gemini-2.5-flash"
        )

        self.client = genai.Client(api_key=api_key)

    def generate_text(self, prompt):
        """
        Standard non-streaming Gemini request.
        Used by LLM #2.
        """

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        if not response.text:
            raise RuntimeError(
                "Gemini returned an empty response."
            )

        return response.text

    def generate_json(self, prompt):
        """
        Generate structured JSON using Gemini.
        Used by LLM #1.
        """

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema={
                    "type": "OBJECT",
                    "properties": {
                        "client_needs": {
                            "type": "ARRAY",
                            "items": {"type": "STRING"},
                        },
                        "pain_points": {
                            "type": "ARRAY",
                            "items": {"type": "STRING"},
                        },
                        "recommended_services": {
                            "type": "ARRAY",
                            "items": {"type": "STRING"},
                        },
                        "key_benefits": {
                            "type": "ARRAY",
                            "items": {"type": "STRING"},
                        },
                        "target_outcomes": {
                            "type": "ARRAY",
                            "items": {"type": "STRING"},
                        },
                    },
                    "required": [
                        "client_needs",
                        "pain_points",
                        "recommended_services",
                        "key_benefits",
                        "target_outcomes",
                    ],
                },
            ),
        )

        if not response.text:
            raise RuntimeError(
                "Gemini returned an empty JSON response."
            )

        return response.text

    def stream_text(self, prompt):
        """
        Stream the final proposal.
        Used by LLM #3.
        """

        response_stream = self.client.models.generate_content_stream(
            model=self.model,
            contents=prompt,
        )

        for chunk in response_stream:
            if chunk.text:
                yield chunk.text