"""
Inspect the chat template used by a Hugging Face chat/instruction tokenizer.

Pipeline:
Messages
    -> tokenizer.apply_chat_template()
    -> rendered prompt containing role/special markers
    -> token IDs
"""

from transformers import AutoTokenizer
import argparse

MODEL_IDS = {
    "phi": "microsoft/phi-4",
    "deepseek": "deepseek-ai/DeepSeek-V3",
    "qwen": "Qwen/Qwen2.5-Coder-0.5B-Instruct",
}

MESSAGES = [
    {
        "role": "system",
        "content": "You are a helpful programming assistant.",
    },
    {
        "role": "user",
        "content": "Explain Python decorators.",
    },
    {
        "role": "assistant",
        "content": (
            "A decorator is a callable that wraps another function or class "
            "to extend its behavior without modifying its original source."
        ),
    },
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tokenizer", choices=MODEL_IDS, default="qwen")
    args = parser.parse_args()

    model_id = MODEL_IDS[args.tokenizer]
    tokenizer = AutoTokenizer.from_pretrained(
        model_id,
        trust_remote_code=(args.tokenizer == "deepseek"),
    )

    print("\nMESSAGES")
    print("=" * 80)
    for message in MESSAGES:
        print(f"{message['role'].upper()}: {message['content']}")

    print("\nCHAT TEMPLATE SOURCE")
    print("=" * 80)
    print(tokenizer.chat_template or "[No chat template exposed by tokenizer]")

    print("\nRENDERED CHAT PROMPT")
    print("=" * 80)
    rendered = tokenizer.apply_chat_template(
        MESSAGES,
        tokenize=False,
        add_generation_prompt=False,
    )
    print(repr(rendered))
    print("\nHuman-readable rendering:\n")
    print(rendered)

    print("\nTOKEN IDS")
    print("=" * 80)
    ids = tokenizer.apply_chat_template(
        MESSAGES,
        tokenize=True,
        add_generation_prompt=False,
    )
    print(ids)
    print(f"\nTotal chat-formatted tokens: {len(ids)}")

    print("\nTOKENS")
    print("=" * 80)
    pieces = tokenizer.convert_ids_to_tokens(ids)
    for i, (token_id, piece) in enumerate(zip(ids, pieces), start=1):
        print(f"{i:>4}  {token_id:>8}  {repr(piece)}")

    print("\nSPECIAL TOKEN SUMMARY")
    print("=" * 80)
    print(tokenizer.special_tokens_map)
    print("All special tokens:", tokenizer.all_special_tokens)
    print("All special IDs   :", tokenizer.all_special_ids)

    print("\nWHY THE TEMPLATE MATTERS")
    print(
        "Instruction models are trained on a specific serialization of roles. "
        "Using the wrong template can remove or misplace role boundaries, "
        "special tokens, stop markers, or generation prompts. The model may "
        "then treat system instructions as ordinary text, continue the wrong "
        "speaker, produce worse answers, or fail to stop where expected."
    )


if __name__ == "__main__":
    main()
