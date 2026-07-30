import time

from providers.gemini import GeminiProvider
from providers.ollama import OllamaProvider
from providers.openrouter import OpenRouterProvider


gemini = GeminiProvider()

ollama = OllamaProvider(model="qwen2.5:latest")

openrouter = OpenRouterProvider()


def ask_model(provider):

    prompt = input("\nEnter Prompt : ")

    start = time.time()

    response = provider.generate(prompt)

    end = time.time()

    print("\n========================")
    print(response)
    print("========================")
    print(f"\nResponse Time : {end-start:.2f} sec")


def compare_models():

    prompt = input("\nPrompt : ")

    print("\nGemini Thinking...\n")

    start = time.time()

    g = gemini.generate(prompt)

    gtime = time.time()-start

    print(g)

    print("\n-----------------------------")

    print("\nOllama Thinking...\n")

    start = time.time()

    o = ollama.generate(prompt)

    otime = time.time()-start

    print(o)

    print("\n-----------------------------")

    print("\nOpenRouter Thinking...\n")

    start = time.time()

    op = openrouter.generate(prompt)

    optime = time.time()-start

    print(op)

    print("\n==========================")

    print("Response Times")

    print(f"Gemini      : {gtime:.2f}")

    print(f"Ollama      : {otime:.2f}")

    print(f"OpenRouter  : {optime:.2f}")


while True:

    print("\n========== AI Playground ==========")

    print("1. Gemini")

    print("2. Ollama")

    print("3. OpenRouter")

    print("4. Compare Models")

    print("0. Exit")

    choice = input("\nChoice : ")

    if choice == "1":

        ask_model(gemini)

    elif choice == "2":

        ask_model(ollama)

    elif choice == "3":

        ask_model(openrouter)

    elif choice == "4":

        compare_models()

    elif choice == "0":

        print("Goodbye")

        break

    else:

        print("Invalid Choice")