import ollama


def ask_ollama(system_prompt, history, message):

    messages = []

    # System Prompt
    messages.append(
        {
            "role": "system",
            "content": system_prompt
        }
    )

    # Conversation History
    for user, assistant in history:

        messages.append(
            {
                "role": "user",
                "content": user
            }
        )

        messages.append(
            {
                "role": "assistant",
                "content": assistant
            }
        )

    # Current Message
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    stream = ollama.chat(
        model="llama3.2",
        messages=messages,
        stream=True
    )

    response = ""

    for chunk in stream:

        text = chunk["message"]["content"]

        response += text

        yield response