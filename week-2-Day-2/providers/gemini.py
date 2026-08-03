import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(prompt):

    stream = client.models.generate_content_stream(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    full = ""

    for chunk in stream:

        if chunk.text:

            full += chunk.text

            yield full