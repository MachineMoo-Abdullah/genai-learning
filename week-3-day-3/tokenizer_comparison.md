# Tokenizer Comparison Analysis

## Models/tokenizers

This project compares tokenizer behavior for:

- Phi-4
- DeepSeek-V3
- Qwen2.5-Coder (instructor)

The full language models are **not** loaded. Only tokenizer files are downloaded.

Run:

```bash
python tokenizer_comparison.py
```

The script writes:

```text
tokenizer_comparison_results.csv
```

## Test set

The comparison includes:

1. `Hello, how are you?`
2. `Generative AI is changing software development.`
3. Python code: `def calculate_sum(a, b): return a + b`
4. `123456789`
5. `Artificial intelligence is amazing!`
6. A technical paragraph
7. Urdu text

## Comparison table

After running the script, copy the measured values into this table.


               Text  Phi  DeepSeek  Qwen
         Sentence 1    6         6     6
         Sentence 2    8         8     8
               Code   11        11    11
            Numbers    3         3     9
         Sentence 5    6         5     6
Technical paragraph   43        43    43
 Non-English (Urdu)   32        17    22

TOTAL TOKENS
Phi         109
DeepSeek     93
Qwen        105

## Questions

### Which tokenizer produces the fewest tokens overall?

Use the **Total** row from the actual experiment.

Do not guess before running the tokenizers, because tokenizer files and model versions determine the result.

### Does the smallest total mean that tokenizer is "better"?

No.

The experiment only measures token-count efficiency on a tiny set of examples.

A tokenizer can be good at English prose but less efficient for code or another language. Another tokenizer may use a larger vocabulary to represent certain patterns compactly. Tokenizers are also tightly coupled to the model that was trained with them.

The meaningful conclusion is:

> "Tokenizer X used the fewest tokens on this specific test set."

It is not:

> "Tokenizer X is universally the best tokenizer."

## What to inspect beyond total count

Compare the token pieces using `tokenizer_explorer.py`.

Look for:

- whole words versus subwords,
- punctuation handling,
- leading-space tokens,
- number grouping,
- identifier splitting in code,
- Urdu segmentation,
- special-token behavior.

This qualitative inspection explains *why* the token counts differ.
