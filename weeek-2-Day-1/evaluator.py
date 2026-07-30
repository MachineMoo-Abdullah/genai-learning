import json
import time
import os

from providers.ollama import OllamaProvider
from providers.openrouter import OpenRouterProvider

# Initialize providers
ollama = OllamaProvider(model="qwen2.5:latest")
openrouter = OpenRouterProvider()

# Load prompts
with open(
    "weeek-2-Day-1/prompts/reasoning_prompts.json",
    "r",
    encoding="utf-8"
) as f:
    prompts = json.load(f)

print("=" * 90)
print("MODEL EVALUATION")
print("=" * 90)

results = []

# Create reports folder if it doesn't exist
os.makedirs("weeek-2-Day-1/reports", exist_ok=True)

for question in prompts:

    title = question["title"]
    prompt = question["prompt"]

    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)

    # ---------------- OLLAMA ----------------

    start = time.time()

    try:
        ollama_response = ollama.generate(prompt)
    except Exception as e:
        ollama_response = f"Error: {e}"

    ollama_time = time.time() - start

    # ---------------- OPENROUTER ----------------

    start = time.time()

    try:
        openrouter_response = openrouter.generate(prompt)
    except Exception as e:
        openrouter_response = f"Error: {e}"

    openrouter_time = time.time() - start

    # ---------------- PRINT ----------------

    print("\nOLLAMA")
    print("-" * 80)
    print(ollama_response)
    print(f"\nResponse Time: {ollama_time:.2f} seconds")

    print("\n" + "-" * 80)

    print("\nOPENROUTER")
    print("-" * 80)
    print(openrouter_response)
    print(f"\nResponse Time: {openrouter_time:.2f} seconds")

    print("\n" + "#" * 90)

    # Save in list
    results.append(
        {
            "title": title,
            "prompt": prompt,
            "ollama": {
                "response": ollama_response,
                "response_time": round(ollama_time, 2),
            },
            "openrouter": {
                "response": openrouter_response,
                "response_time": round(openrouter_time, 2),
            },
        }
    )

# =====================================================
# Save JSON Report
# =====================================================

json_path = "/Applications/genai-learning/weeek-2-Day-1/prompts/reasoning_prompts.json"

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

print(f"\nJSON report saved to:\n{json_path}")

# =====================================================
# Save Markdown Report
# =====================================================

md_path = "/Applications/genai-learning/weeek-2-Day-1/reports/reasoning.md"

with open(md_path, "w", encoding="utf-8") as f:

    f.write("# Reasoning Benchmark Report\n\n")

    f.write("## Models Compared\n\n")
    f.write("- Ollama (Qwen 2.5)\n")
    f.write("- OpenRouter\n\n")

    for item in results:

        f.write(f"# {item['title']}\n\n")

        f.write("## Prompt\n\n")
        f.write(item["prompt"] + "\n\n")

        f.write("## Ollama Response\n\n")
        f.write(item["ollama"]["response"] + "\n\n")
        f.write(
            f"**Response Time:** {item['ollama']['response_time']} seconds\n\n"
        )

        f.write("---\n\n")

        f.write("## OpenRouter Response\n\n")
        f.write(item["openrouter"]["response"] + "\n\n")
        f.write(
            f"**Response Time:** {item['openrouter']['response_time']} seconds\n\n"
        )

        f.write("============================================================\n\n")

print(f"Markdown report saved to:\n{md_path}")

print("\nEvaluation completed successfully!")