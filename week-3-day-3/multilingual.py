from transformers import AutoTokenizer
import pandas as pd

MODELS = {
    "Phi": "microsoft/phi-4",
    "DeepSeek": "deepseek-ai/DeepSeek-V3",
    "Qwen": "Qwen/Qwen2.5-Coder-0.5B-Instruct",
}

TEXTS = {
    "English": "Artificial intelligence is changing the world.",
    "Urdu": "مصنوعی ذہانت دنیا کو بدل رہی ہے۔",
    "Arabic": "الذكاء الاصطناعي يغير العالم.",
    "Chinese": "人工智能正在改变世界。",
}

rows = []

for model_name, model_id in MODELS.items():
    tokenizer = AutoTokenizer.from_pretrained(
        model_id,
        trust_remote_code=(model_name == "DeepSeek"),
    )

    for language, text in TEXTS.items():
        ids = tokenizer.encode(text, add_special_tokens=False)
        rows.append({
            "Tokenizer": model_name,
            "Language": language,
            "Characters": len(text),
            "Tokens": len(ids),
        })

df = pd.DataFrame(rows)
print(df.pivot(index="Language", columns="Tokenizer", values="Tokens"))