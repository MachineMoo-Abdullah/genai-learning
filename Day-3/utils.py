import requests
from openai import AuthenticationError, RateLimitError
def select_model():

    print("\nChoose Model")
    print("1. Qwen 3 (Groq)")
    print("2. Llama 3.3 (Groq)")

    while True:
        try:
            choice = int(input("Choice: "))

            if choice in [1, 2, 3]:
                return choice

            print("Invalid choice.")

        except ValueError:
            print("Please enter a number.")

def display_response(response):

    print("\nAI:")
    print(response)
    print()


def handle_error(error):

    if isinstance(error, AuthenticationError):
        print("Invalid API Key.")

    elif isinstance(error, RateLimitError):
        print("Rate limit exceeded.")

    elif isinstance(error, requests.ConnectionError):
        print("No Internet Connection.")

    elif isinstance(error, requests.Timeout):
        print("Request Timed Out.")

    else:
        print(error)