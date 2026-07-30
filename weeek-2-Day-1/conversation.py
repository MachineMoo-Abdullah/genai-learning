import os

from providers.openrouter import OpenRouterProvider
from providers.ollama import OllamaProvider


openrouter = OpenRouterProvider()
ollama = OllamaProvider()


def ai_vs_ai(topic, rounds=5):

    history = []

    print("=" * 80)
    print("AI vs AI Conversation")
    print("=" * 80)

    print(f"\nTopic : {topic}\n")

    # First response from OpenRouter
    openrouter_response = openrouter.generate(
        f"""
Topic: {topic}

Give your opinion in about 150 words.
"""
    )

    print("\nOpenRouter\n")
    print(openrouter_response)

    history.append(("OpenRouter", openrouter_response))

    for i in range(rounds):

        ollama_prompt = f"""
You are debating another AI.

Topic:
{topic}

OpenRouter said:

{openrouter_response}

Respond respectfully with improvements,
counterarguments or agreements.
"""

        ollama_response = ollama.generate(ollama_prompt)

        print("\n")
        print("=" * 80)
        print(f"Round {i+1}")
        print("=" * 80)

        print("\nOllama\n")
        print(ollama_response)

        history.append(("Ollama", ollama_response))

        openrouter_prompt = f"""
Topic:

{topic}

Ollama replied:

{ollama_response}

Critique the answer and improve your own response.
"""

        openrouter_response = openrouter.generate(openrouter_prompt)

        print("\nOpenRouter\n")
        print(openrouter_response)

        history.append(("OpenRouter", openrouter_response))

    os.makedirs("reports", exist_ok=True)

    with open(
        "reports/conversation.md",
        "w",
        encoding="utf-8"
    ) as file:

        file.write("# AI vs AI Conversation\n\n")

        file.write(f"## Topic\n\n{topic}\n\n")

        for speaker, text in history:

            file.write(f"## {speaker}\n\n")
            file.write(text)
            file.write("\n\n---\n\n")

    print("\nConversation saved to reports/conversation.md")


if __name__ == "__main__":

    print("\nTopics")
    print("1. Should AI replace software engineers?")
    print("2. Is remote work better than office work?")
    print("3. REST vs GraphQL")
    print("4. Python vs Rust")

    choice = input("\nChoose : ")

    topics = {
        "1": "Should AI replace software engineers?",
        "2": "Is remote work better than office work?",
        "3": "REST vs GraphQL",
        "4": "Python vs Rust"
    }

    topic = topics.get(choice)

    if topic:
        ai_vs_ai(topic)
    else:
        print("Invalid Choice")