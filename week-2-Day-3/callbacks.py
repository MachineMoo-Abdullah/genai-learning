import os

from providers.gemini import ask_gemini
from providers.ollama import ask_ollama

from providers.gemini import ask_gemini
from providers.ollama import ask_ollama
from prompts import SYSTEM_PROMPTS, PROMPT_TEMPLATES

from document_loader import load_document
from rag import build_prompt

def generate_response(

    prompt,
    history,
    assistant,
    model,
    template,
    document

):

    history = history or []

    system_prompt = SYSTEM_PROMPTS[assistant]

    template_prompt = PROMPT_TEMPLATES[template]

    document_text = load_document(document)
    user_prompt = prompt

    prompt = build_prompt(

        document_text,

        user_prompt

    )

    final_prompt = template_prompt + "\n\n" + prompt

    if user_prompt.strip() == "/history":
        text = ""

        for msg in history:

            text += f"{msg['role'].upper()}:\n{msg['content']}\n\n"

        history.append({
            "role": "assistant",
            "content": text if text else "No conversation yet."
        })

        yield history, history
        return


    if user_prompt.strip() == "/clear":

        history.clear()

        yield history, history
        return


    if user_prompt.strip() == "/save":

        save_chat(history)

        history.append({

            "role": "assistant",

            "content": "Conversation saved successfully."

        })

        yield history, history
        return

    if model == "Gemini":
        stream = ask_gemini(
            system_prompt,
            history,
            final_prompt
        )
    else:
        stream = ask_ollama(

            system_prompt,
            history,
            final_prompt

        )

    history.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    history.append(
        {
            "role": "assistant",
            "content": ""
        }
    )

    for partial in stream:

        history[-1]["content"] = partial

        yield history, history


from pathlib import Path

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

CHAT_FILE = OUTPUT_DIR / "chat_history.md"

def load_chat():

    history = []

    if not CHAT_FILE.exists():
        return history

    role = None
    content = []

    with open(CHAT_FILE, "r", encoding="utf-8") as f:

        for line in f:

            line = line.rstrip()

            if line == "## User":

                if role:

                    history.append({
                        "role": role,
                        "content": "\n".join(content)
                    })

                role = "user"
                content = []

            elif line == "## Assistant":

                if role:

                    history.append({
                        "role": role,
                        "content": "\n".join(content)
                    })

                role = "assistant"
                content = []

            elif line.startswith("# AI Assistant"):
                continue

            else:
                content.append(line)

        if role:

            history.append({

                "role": role,

                "content": "\n".join(content)

            })

    return history
def clear_chat():
    return ""

def reset_chat():

    if os.path.exists(CHAT_FILE):
        os.remove(CHAT_FILE)

    return [], [], "Chat Reset Successfully."


def save_chat(history):

    with open(CHAT_FILE, "w", encoding="utf-8") as f:

        f.write("# AI Assistant Conversation\n\n")

        for message in history:

            if message["role"] == "user":

                f.write(f"## User\n")

            else:

                f.write(f"## Assistant\n")

            f.write(message["content"])
            f.write("\n\n")

    return "Conversation saved."