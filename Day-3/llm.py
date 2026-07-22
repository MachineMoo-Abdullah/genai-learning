import re

import requests
from openai import OpenAI

from config import *

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def ask_groq(history, model_name):

    response = client.chat.completions.create(
        model=model_name,
        messages=history,
    )
    content = response.choices[0].message.content

    # Remove thinking tags if present
    content = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()

    return content



def send_prompt(model, history):

    if model == 1:
        # Qwen
        return ask_groq(history, "qwen/qwen3.6-27b")

    elif model == 2:
        # Llama
        return ask_groq(history, "llama-3.3-70b-versatile")

    else:
        raise ValueError("Invalid model.")