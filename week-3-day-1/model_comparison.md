# Model Comparison

## Models

- Model A: `Qwen/Qwen2.5-0.5B-Instruct`
- Model B: `HuggingFaceTB/SmolLM2-360M-Instruct`

## Hardware

The notebook records the actual Colab device/GPU.

## Objective metrics

Metric	Model A	Model B
0	Average response time (s)	3.662182	4.581736
1	Average generated tokens	100.000000	82.300000
2	Average GPU memory (GB)	2.556566	2.554115
3	Response quality (subjective)	4.000000	4.000000
4	Instruction following (subjective)	4.000000	4.000000
5	Coding quality (subjective)	3.000000	3.000000
6	Reasoning (subjective)	3.000000	3.000000


## Subjective metrics

Scores use a 1–5 rubric:

- 1 = very poor
- 2 = poor
- 3 = acceptable
- 4 = good
- 5 = excellent

| Metric | Model A | Model B |
|---|---:|---:|
| Response quality | 4 | 3 |
| Instruction following | 5 | 2 |
| Coding quality | 3 | 3 |
| Reasoning | 4 | 3 |

These are human judgments, not objective benchmark measurements.

## Prompts

The notebook uses exactly 10 prompts:


comparison_prompts = [
    ("General", "What is artificial intelligence?"),
    ("General", "Explain machine learning to a beginner."),
    ("General", "What is a neural network?"),
    ("General", "Why are GPUs useful for AI?"),
    ("General", "What is the difference between training and inference?"),
    ("Coding", "Write a Python function that calculates the factorial of a number."),
    ("Coding", "Write Python code to find the largest number in a list."),
    ("Reasoning", "If a model processes 100 tokens per second, how many tokens can it process in 10 seconds?"),
    ("Reasoning", "A box contains 3 red balls and 2 blue balls. What is the probability of selecting a red ball?"),
    ("Creative", "Write a short story about a robot that becomes a software engineer.")
]
