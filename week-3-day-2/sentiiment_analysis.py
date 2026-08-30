from transformers import pipeline
import time


def main():
    print("=" * 70)
    print("SENTIMENT ANALYSIS EXPERIMENT")
    print("=" * 70)

    device = 0  # GPU
    # Change to -1 if running without GPU

    classifier = pipeline(
        "sentiment-analysis",
        device=device
    )

    test_cases = [
        # Positive
        ("I absolutely love this product. It is fantastic!", "POSITIVE"),
        ("The service was excellent and the staff were very helpful.", "POSITIVE"),
        ("This is the best experience I have ever had.", "POSITIVE"),

        # Negative
        ("I hate this product. It was a complete waste of money.", "NEGATIVE"),
        ("The application keeps crashing and nothing works.", "NEGATIVE"),
        ("I am extremely disappointed with the poor quality.", "NEGATIVE"),

        # Neutral
        ("The package was delivered on Tuesday.", "NEUTRAL"),
        ("The company released a new version of the software.", "NEUTRAL"),
        ("The meeting will start at 10 AM tomorrow.", "NEUTRAL"),

        # Sarcastic
        ("Great, another software update that broke everything.", "NEGATIVE"),
        ("Wonderful! My internet stopped working again.", "NEGATIVE"),
        ("Oh fantastic, I just lost all my work.", "NEGATIVE"),

        # Mixed
        ("The design looks beautiful, but the performance is terrible.", "NEGATIVE"),
        ("The product is expensive, but the quality is excellent.", "POSITIVE"),
        ("I like the idea, although the implementation needs improvement.", "POSITIVE"),
    ]

    correct = 0
    results = []

    print("\nRunning predictions...\n")

    for i, (text, expected) in enumerate(test_cases, start=1):
        start = time.perf_counter()

        prediction = classifier(text)[0]

        elapsed = time.perf_counter() - start

        label = prediction["label"]
        confidence = prediction["score"]

        # The default model normally predicts POSITIVE/NEGATIVE.
        # For neutral examples, we record whether the model can match
        # the manually expected interpretation.
        is_correct = label == expected

        if is_correct:
            correct += 1

        results.append({
            "input": text,
            "predicted": label,
            "confidence": confidence,
            "expected": expected,
            "correct": is_correct,
            "time": elapsed
        })

        print(f"{i}. Input: {text}")
        print(f"   Predicted: {label}")
        print(f"   Confidence: {confidence:.4f}")
        print(f"   Expected: {expected}")
        print(f"   Result: {'Correct ✓' if is_correct else 'Incorrect ✗'}")
        print()

    accuracy = correct / len(test_cases)

    print("=" * 70)
    print(f"Correct Predictions: {correct}/{len(test_cases)}")
    print(f"Accuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)")
    print("=" * 70)

    print("\nIMPORTANT OBSERVATION:")
    print(
        "A high confidence score does NOT prove that the prediction is correct. "
        "Confidence represents how strongly the model prefers its prediction."
    )


if __name__ == "__main__":
    main()