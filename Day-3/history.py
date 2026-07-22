import json
import os

FILE_NAME = "chat_history.json"


def load_chat_history():

    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_chat_history(history):

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)


def show_chat_history(history):

    if not history:
        print("\nNo previous chat history.\n")
        return

    print("\n========== Chat History ==========\n")

    for message in history:

        if message["role"] == "user":
            print(f"User: {message['content']}")

        elif message["role"] == "assistant":
            print(f"AI: {message['content']}")

        print()

    print("==================================\n")