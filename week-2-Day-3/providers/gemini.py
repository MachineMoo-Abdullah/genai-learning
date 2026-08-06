import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(system_prompt, history, message):

    contents = []

    # System Prompt
    contents.append(
        {
            "role": "user",
            "parts": [{"text": system_prompt}]
        }
    )

    # Conversation History
    for user, assistant in history:

        contents.append(
            {
                "role": "user",
                "parts": [{"text": user}]
            }
        )

        contents.append(
            {
                "role": "model",
                "parts": [{"text": assistant}]
            }
        )

    # Current Message
    contents.append(
        {
            "role": "user",
            "parts": [{"text": message}]
        }
    )

    stream = client.models.generate_content_stream(
        model="gemini-3.5-flash",
        contents=contents
    )

    response = ""

    for chunk in stream:

        if chunk.text:

            response += chunk.text

            yield response