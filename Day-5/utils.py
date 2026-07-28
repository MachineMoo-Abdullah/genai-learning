import json
from google import genai
from dotenv import load_dotenv
import os
from prompts import LINK_SELECTION_PROMPT

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))


def get_relevant_links(page_text, links):

    prompt = f"""
    {LINK_SELECTION_PROMPT}

    Landing Page Text:
    {page_text}

    Hyperlinks:
    {links}
    """
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
    )

    return json.loads(response.text)

