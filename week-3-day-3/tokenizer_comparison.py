

from transformers import AutoTokenizer
import pandas as pd

MODEL_IDS = {
    "Phi": "microsoft/phi-4",
    "DeepSeek": "deepseek-ai/DeepSeek-V3",
    "Qwen": "Qwen/Qwen2.5-Coder-0.5B-Instruct",
}

TEST_TEXTS = {
    "Sentence 1": "Hello, how are you?",
    "Sentence 2": "Generative AI is changing software development.",
    "Code": "def calculate_sum(a, b): return a + b",
    "Numbers": "123456789",
    "Sentence 5": "Artificial intelligence is amazing!",
    "Technical paragraph": (
        "Large language models transform text into numerical token IDs before "
        "processing it with transformer layers. Tokenization therefore affects "
        "the effective context length, computational work, and the amount of "
        "text that can be represented inside a fixed token budget."
    ),
    "Non-English (Urdu)": "مصنوعی ذہانت دنیا کو بدل رہی ہے۔",
}


def safe_load(name, model_id):
    try:
        print(f"Loading {name}: {model_id}")
        return AutoTokenizer.from_pretrained(
            model_id,
            trust_remote_code=(name == "DeepSeek"),
        )
    except Exception as e:
        print(f"WARNING: {name} could not be loaded.")
        print(e)
        if name == "Llama":
            print(
                "Accept the Llama license on Hugging Face and run "
                "`huggingface-cli login`, then retry."
            )
        return None


def count_tokens(tokenizer, text):
    # No chat formatting here: compare raw-text tokenization.
    return len(tokenizer.encode(text, add_special_tokens=False))


def main():
    tokenizers = {
        name: safe_load(name, model_id)
        for name, model_id in MODEL_IDS.items()
    }

    rows = []
    for label, text in TEST_TEXTS.items():
        row = {"Text": label, "Sample": text}
        for name, tokenizer in tokenizers.items():
            row[name] = (
                count_tokens(tokenizer, text)
                if tokenizer is not None
                else None
            )
        rows.append(row)

    df = pd.DataFrame(rows)

    print("\nTOKEN COUNTS")
    print("=" * 90)
    print(df[["Text", *MODEL_IDS.keys()]].to_string(index=False))

    totals = df[list(MODEL_IDS.keys())].sum(axis=0, skipna=False)

    print("\nTOTAL TOKENS")
    print("=" * 90)
    print(totals)

    available_totals = totals.dropna()
    if len(available_totals):
        winner = available_totals.idxmin()
        print(
            f"\nFewest tokens across this small test set: "
            f"{winner} ({int(available_totals[winner])} tokens)"
        )
        print(
            "Important: this does NOT prove that this tokenizer is universally "
            "better. Efficiency varies by language/domain, and tokenizer design "
            "also trades off vocabulary size, representation quality, compatibility, "
            "and model training choices."
        )

    output = "tokenizer_comparison_results.csv"
    df.to_csv(output, index=False)
    print(f"\nSaved: {output}")


if __name__ == "__main__":
    main()
