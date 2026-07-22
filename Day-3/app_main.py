import llm

from history import *
from llm import *
from utils import *


def main():

    print("LLM Chat Application")

    model = select_model()

    history = load_chat_history()
    show_chat_history(history)
    while True:
        prompt = input("\nEnter your question (exit to quit): ")

        if prompt.lower() == "exit":
            save_chat_history(history)
            print("Chat saved.")
            break

        if prompt.strip() == "":
            print("Prompt cannot be empty.")
            continue

        history.append({
            "role": "user",
            "content": prompt
        })

        try:

            answer = llm.send_prompt(model, history)

            history.append({
                "role": "assistant",
                "content": answer
            })

            display_response(answer)

            save_chat_history(history)

        except Exception as e:

            handle_error(e)


if __name__ == "__main__":
    main()