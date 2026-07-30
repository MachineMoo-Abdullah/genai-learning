import json
import os
import time

from providers.ollama import OllamaProvider
from providers.openrouter import OpenRouterProvider


llama = OllamaProvider(model="llama3.2:latest")
openrouter = OpenRouterProvider()

# Load Brain Teasers
with open(
    "/Applications/genai-learning/weeek-2-Day-1/prompts/ brain_teasers.json",
    "r",
    encoding="utf-8"
) as f:
    teasers = json.load(f)

os.makedirs("reports", exist_ok=True)

results = []

print("=" * 90)
print("BRAIN TEASER EVALUATION")
print("=" * 90)

for teaser in teasers:

    title = f"Brain Teaser {teaser['id']}"
    prompt = teaser["question"]
    answer = teaser["answer"]

    print("\n" + "=" * 90)
    print(title)
    print("=" * 90)

    # ---------------- LLAMA ----------------

    start = time.time()

    try:
        llama_response = llama.generate(prompt)
    except Exception as e:
        llama_response = f"Error : {e}"

    llama_time = time.time() - start

    # ---------------- OPENROUTER ----------------

    start = time.time()

    try:
        openrouter_response = openrouter.generate(prompt)
    except Exception as e:
        openrouter_response = f"Error : {e}"

    openrouter_time = time.time() - start

    # Print Results

    print("\nCorrect Answer")
    print(answer)

    print("\nLlama")
    print(llama_response)
    print(f"Time : {llama_time:.2f}s")

    print("\n" + "-" * 80)

    print("\nOpenRouter")
    print(openrouter_response)
    print(f"Time : {openrouter_time:.2f}s")

    # Store Results

    results.append(
        {
            "title": title,
            "prompt": prompt,
            "correct_answer": answer,
            "llama": {
                "response": llama_response,
                "time": round(llama_time, 2),
            },
            "openrouter": {
                "response": openrouter_response,
                "time": round(openrouter_time, 2),
            },
        }
    )


# ==========================================================
# Save Markdown Report
# ==========================================================

with open(
    "/Applications/genai-learning/weeek-2-Day-1/reports/brain-teasor.md",
    "w",
    encoding="utf-8"
) as f:

    f.write("# Brain Teaser Evaluation Report\n\n")

    f.write("| Brain Teaser | Correct Answer | Llama | OpenRouter |\n")
    f.write("|--------------|----------------|-------|------------|\n")

    for item in results:

        llama_short = item["llama"]["response"].replace("\n", " ")[:120]
        openrouter_short = item["openrouter"]["response"].replace("\n", " ")[:120]

        f.write(
            f"| {item['title']} | "
            f"{item['correct_answer']} | "
            f"{llama_short} | "
            f"{openrouter_short} |\n"
        )

    f.write("\n\n---\n\n")

    for item in results:

        f.write(f"# {item['title']}\n\n")

        f.write("## Question\n\n")
        f.write(item["prompt"] + "\n\n")

        f.write("## Correct Answer\n\n")
        f.write(item["correct_answer"] + "\n\n")

        f.write("## Llama\n\n")
        f.write(item["llama"]["response"] + "\n\n")
        f.write(f"Response Time: {item['llama']['time']} sec\n\n")

        f.write("## OpenRouter\n\n")
        f.write(item["openrouter"]["response"] + "\n\n")
        f.write(f"Response Time: {item['openrouter']['time']} sec\n\n")

        f.write("## Best Model\n\n")
        f.write("To be evaluated manually.\n\n")

        f.write("## Common Mistakes\n\n")
        f.write("To be evaluated manually.\n\n")

        f.write("---\n\n")

print("Markdown report saved.")

print("\nEvaluation Completed Successfully!")