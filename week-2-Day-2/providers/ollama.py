import ollama


def ask_ollama(prompt):

    response = ""

    stream = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        stream=True
    )

    for chunk in stream:

        text = chunk["message"]["content"]

        response += text

        yield response