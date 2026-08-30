from transformers import pipeline


def generate_text(generator, prompt, **kwargs):

    result = generator(
        prompt,
        **kwargs
    )

    return result[0]["generated_text"]


def main():

    print("=" * 70)
    print("TEXT GENERATION EXPERIMENT")
    print("=" * 70)

    generator = pipeline(
        "text-generation",
        model="distilgpt2",
        device=0
    )

    prompt = "Write a short product description for an AI receptionist:"

    experiments = [
        {
            "name": "Short deterministic generation",
            "params": {
                "max_new_tokens": 30,
                "do_sample": False
            }
        },
        {
            "name": "Creative generation",
            "params": {
                "max_new_tokens": 60,
                "do_sample": True,
                "temperature": 0.7
            }
        },
        {
            "name": "More random generation",
            "params": {
                "max_new_tokens": 60,
                "do_sample": True,
                "temperature": 1.2
            }
        }
    ]

    for experiment in experiments:

        print("\n" + "-" * 70)
        print(experiment["name"])
        print("Parameters:", experiment["params"])
        print("-" * 70)

        output = generate_text(
            generator,
            prompt,
            **experiment["params"]
        )

        print(output)

    print("\n" + "=" * 70)
    print("PARAMETER OBSERVATIONS")
    print("=" * 70)
    print("max_new_tokens: Controls the maximum amount of new text.")
    print("do_sample=False: Usually produces more deterministic output.")
    print("do_sample=True: Allows sampling and more variation.")
    print("Lower temperature: Usually more predictable output.")
    print("Higher temperature: Usually more random and creative output.")


if __name__ == "__main__":
    main()