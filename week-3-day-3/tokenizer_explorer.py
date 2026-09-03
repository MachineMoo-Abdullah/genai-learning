"""
Week 3 - Day 3
LLM Tokenizer Explorer

Loads a selected Hugging Face tokenizer and shows:
- character count
- word count
- token count
- token pieces
- token IDs
- encode/decode reconstruction
- special tokens

Only tokenizers are loaded; model weights are NOT downloaded.
"""

from transformers import AutoTokenizer
import argparse
import re

MODEL_IDS = {
    "phi": "microsoft/phi-4",
    "deepseek": "deepseek-ai/DeepSeek-V3",
    "qwen": "Qwen/Qwen2.5-Coder-0.5B-Instruct",
}


def load_tokenizer(name: str):
    name = name.lower()
    if name not in MODEL_IDS:
        raise ValueError(f"Unknown tokenizer: {name}. Choose from {list(MODEL_IDS)}")

    model_id = MODEL_IDS[name]
    print(f"\nLoading tokenizer: {name} -> {model_id}")

    try:
        return AutoTokenizer.from_pretrained(
            model_id,
            trust_remote_code=(name == "deepseek"),
        )
    except Exception as e:
        if name == "llama":
            print("\nLlama access note:")
            print("The official Llama repository may require accepting Meta's license")
            print("on Hugging Face and logging in with: huggingface-cli login")
        raise RuntimeError(f"Could not load {model_id}: {e}") from e


def visible_token(token: str) -> str:
    """Make whitespace/control characters easier to inspect."""
    return (
        token
        .replace("\n", "\\n")
        .replace("\t", "\\t")
        .replace(" ", "␠")
    )


def analyze_text(text: str, tokenizer, add_special_tokens: bool = False):
    token_ids = tokenizer.encode(text, add_special_tokens=add_special_tokens)
    token_pieces = tokenizer.convert_ids_to_tokens(token_ids)

    print("\n" + "=" * 72)
    print("TOKENIZER ANALYSIS")
    print("=" * 72)
    print(f"Text       : {text}")
    print(f"Characters : {len(text)}")
    print(f"Words      : {len(re.findall(r'\\S+', text))}")
    print(f"Tokens     : {len(token_ids)}")
    print(f"Specials   : {'included' if add_special_tokens else 'not included'}")

    print("\nTOKEN BREAKDOWN")
    print("-" * 72)
    print(f"{'#':<5}{'Token ID':<12}{'Tokenizer piece'}")
    print("-" * 72)

    for i, (token_id, piece) in enumerate(zip(token_ids, token_pieces), start=1):
        print(f"{i:<5}{token_id:<12}{visible_token(piece)}")

    decoded = tokenizer.decode(token_ids, skip_special_tokens=False)

    print("\nENCODING")
    print(token_ids)

    print("\nDECODING")
    print(decoded)

    print("\nRECONSTRUCTION CHECK")
    if decoded == text:
        print("PASS: decode(encode(text)) exactly reconstructs the original text.")
    else:
        print("NOTE: decoded output is not byte-for-byte identical.")
        print("This can happen because tokenizers may normalize spaces or add special tokens.")

    return {
        "characters": len(text),
        "words": len(re.findall(r"\S+", text)),
        "tokens": len(token_ids),
        "token_ids": token_ids,
        "token_pieces": token_pieces,
        "decoded": decoded,
    }


def show_special_tokens(tokenizer):
    print("\n" + "=" * 72)
    print("SPECIAL TOKENS")
    print("=" * 72)

    fields = [
        ("BOS", tokenizer.bos_token, tokenizer.bos_token_id),
        ("EOS", tokenizer.eos_token, tokenizer.eos_token_id),
        ("PAD", tokenizer.pad_token, tokenizer.pad_token_id),
        ("UNK", tokenizer.unk_token, tokenizer.unk_token_id),
        ("SEP", tokenizer.sep_token, tokenizer.sep_token_id),
        ("CLS", tokenizer.cls_token, tokenizer.cls_token_id),
        ("MASK", tokenizer.mask_token, tokenizer.mask_token_id),
    ]

    for name, token, token_id in fields:
        print(f"{name:<6} token={repr(token):<35} id={token_id}")

    print("\nAll special tokens:")
    print(tokenizer.all_special_tokens)

    print("\nAll special token IDs:")
    print(tokenizer.all_special_ids)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--tokenizer",
        choices=MODEL_IDS.keys(),
        default="qwen",
        help="Tokenizer family to inspect",
    )
    parser.add_argument(
        "--text",
        default="Generative AI is changing software development.",
    )
    parser.add_argument(
        "--specials",
        action="store_true",
        help="Include tokenizer-defined special tokens during encode()",
    )
    args = parser.parse_args()

    tokenizer = load_tokenizer(args.tokenizer)
    analyze_text(args.text, tokenizer, add_special_tokens=args.specials)
    show_special_tokens(tokenizer)


if __name__ == "__main__":
    main()
