# Multilingual Tokenization Experiment

## Goal

Compare tokenizer efficiency across equivalent or near-equivalent sentences written in different languages/scripts.

Use:

### English

```text
Artificial intelligence is changing the world.
```

### Urdu

```text
مصنوعی ذہانت دنیا کو بدل رہی ہے۔
```

### Arabic

```text
الذكاء الاصطناعي يغير العالم.
```

### Chinese

```text
人工智能正在改变世界。
```

## Suggested code

```python
from transformers import AutoTokenizer
import pandas as pd

MODELS = {
    "Llama": "meta-llama/Llama-3.1-8B-Instruct",
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
```

## Results table

Fill this after running the experiment.

Tokenizer  DeepSeek  Phi  Qwen
Language                      
Arabic           11   20    13
Chinese           5   12     5
English           7    8     8
Urdu             17   32    22

## Analysis

Different languages may produce different token counts because tokenizer vocabularies do not cover every script and word pattern equally.

A tokenizer trained with strong coverage of a language may contain common character sequences or words as reusable vocabulary pieces. A tokenizer with less efficient coverage may decompose the same sentence into many smaller pieces.

Other factors include:

- Unicode/script characteristics,
- whitespace conventions,
- vocabulary construction,
- training-corpus composition,
- byte-level fallback behavior,
- normalization choices.

## Important limitation

This is an experiment, not a universal language benchmark.

Four short sentences cannot establish that one tokenizer is always more efficient for English, Urdu, Arabic, or Chinese. A proper benchmark would require a large, balanced dataset containing multiple domains and text lengths.
