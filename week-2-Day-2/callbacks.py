import os
from providers.gemini import ask_gemini


from providers.factorry import get_provider


def generate_response(prompt, history, model):

    if history is None:
        history = []

    history = history.copy()

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

    provider = get_provider(model)

    for chunk in provider(prompt):

        history[-1]["content"] = chunk

        yield history.copy(), history.copy()

def load_chat():

    history = []

    if not os.path.exists("chat_history.txt"):
        return history

    with open("chat_history.txt", "r", encoding="utf-8") as f:

        role = None
        text = []

        for line in f:

            line = line.rstrip()

            if line.startswith("user:"):

                if role is not None:
                    history.append(
                        {
                            "role": role,
                            "content": "\n".join(text)
                        }
                    )

                role = "user"
                text = [line[5:].strip()]

            elif line.startswith("assistant:"):

                if role is not None:
                    history.append(
                        {
                            "role": role,
                            "content": "\n".join(text)
                        }
                    )

                role = "assistant"
                text = [line[10:].strip()]

            else:
                text.append(line)

        if role is not None:

            history.append(
                {
                    "role": role,
                    "content": "\n".join(text)
                }
            )

    return history


def clear_fields():

    return ""


def reset_chat():

    if os.path.exists("chat_history.txt"):
        os.remove("chat_history.txt")

    return "", [], []


def save_chat(history):

    with open("chat_history.txt", "w", encoding="utf-8") as f:

        for message in history:

            f.write(
                f"{message['role']}: {message['content']}\n"
            )

    return "Chat saved successfully."