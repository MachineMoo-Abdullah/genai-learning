from providers.gemini import ask_gemini
from providers.ollama import ask_ollama


def get_provider(model_name):

    providers = {
        "Gemini": ask_gemini,
        "Ollama": ask_ollama
    }

    return providers[model_name]