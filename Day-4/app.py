import ollama
import time

# Available models
models = {
    "1": "llama3.2",
    "2": "qwen2.5",
    "3": "mistral"
}

print("=" * 50)
print(" Multi-Model Chat Application ")
print("=" * 50)
print("Choose a model:")
print("1. Llama")
print("2. Qwen")
print("3. Mistral")

choice = input("\nEnter your choice (1-3): ")

# Handle invalid model selection
if choice not in models:
    print("\nInvalid model selection!")
    print("Please run the program again and choose 1, 2, or 3.")
    exit()

model = models[choice]

print(f"\nUsing model: {model}")
print("Type 'exit' to end the conversation.\n")

# Store conversation history
chat_history = []

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("\nConversation Ended.")
        break

    # Show chat history
    if user_input.lower() == "history":
        print("\n------ Chat History ------")

        if len(chat_history) == 0:
            print("No conversation yet.")

        else:
            for message in chat_history:
                role = message["role"].capitalize()
                print(f"{role}: {message['content']}")

        print("--------------------------\n")
        continue

    # Add user message to history
    chat_history.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    start_time = time.time()

    try:
        response = ollama.chat(
            model=model,
            messages=chat_history
        )

        end_time = time.time()

        assistant_reply = response["message"]["content"]

        print("\nAssistant:")
        print(assistant_reply)

        print(f"\nResponse Time: {end_time - start_time:.2f} seconds\n")

        # Save assistant reply
        chat_history.append(
            {
                "role": "assistant",
                "content": assistant_reply
            }
        )

    except Exception as e:
        print("\nError:", e)
        break