from transformers import pipeline


def main():
    print("=" * 70)
    print("NAMED ENTITY RECOGNITION")
    print("=" * 70)

    ner_pipeline = pipeline(
        "ner",
        aggregation_strategy="simple",
        device=0
    )

    text = """
    Microsoft opened a new AI research center in London in 2026.
    Satya Nadella announced the project during a conference organized
    by the World Economic Forum on January 15, 2026.
    Researchers from Google and OpenAI also attended the event.
    """

    print("\nInput Paragraph:")
    print(text)

    entities = ner_pipeline(text)

    print("\nExtracted Entities:")
    print("-" * 70)

    for entity in entities:
        print(
            f"Entity: {entity['word']:<25} "
            f"Type: {entity['entity_group']:<10} "
            f"Confidence: {entity['score']:.4f}"
        )


if __name__ == "__main__":
    main()