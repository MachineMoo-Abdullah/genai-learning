import tiktoken


def get_encoding():
    """
    Load the GPT tokenizer.
    cl100k_base is commonly used for GPT-style token counting.
    """
    return tiktoken.get_encoding("cl100k_base")


def count_text(text, encoding):
    """Return character, word, and token counts."""
    character_count = len(text)
    word_count = len(text.split())
    token_count = len(encoding.encode(text))

    return character_count, word_count, token_count


def main():
    encoding = get_encoding()

    print("=" * 50)
    print("TOKEN COUNTER")
    print("=" * 50)

    text = input("\nEnter a sentence: ")

    characters, words, tokens = count_text(text, encoding)

    print("\nResults")
    print("-" * 30)
    print(f"Character count : {characters}")
    print(f"Word count      : {words}")
    print(f"Token count     : {tokens}")

    print("\nComparison of different sentences")
    print("-" * 50)

    sentences = [
        "Hello world!",
        "Artificial intelligence is changing the world.",
        "Transformers use self-attention mechanisms.",
        "Tokenization converts text into smaller units called tokens.",
        "Physics-informed multimodal Earth observation models combine SAR, optical, and LiDAR data.",
    ]

    for sentence in sentences:
        characters, words, tokens = count_text(sentence, encoding)

        print(f"\nSentence: {sentence}")
        print(f"Characters: {characters}")
        print(f"Words:      {words}")
        print(f"Tokens:     {tokens}")


if __name__ == "__main__":
    main()