import json
from google import genai
from dotenv import load_dotenv
import os
from prompts import BROCHURE_PROMPT
from utils import client

def generate_brochure(document):
    print("Generating brochure...")
    prompt = f"""
    {BROCHURE_PROMPT}

    Website Content:

    {document}
    """
    print("Generating brochure...")
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text