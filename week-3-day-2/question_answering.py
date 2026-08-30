from transformers import pipeline


def main():
    print("=" * 70)
    print("QUESTION ANSWERING EXPERIMENT")
    print("=" * 70)

    qa_pipeline = pipeline(
        "question-answering",
        device=0
    )

    context = """
    Artificial intelligence is a field of computer science focused on
    creating systems capable of performing tasks that normally require
    human intelligence. These tasks can include learning, reasoning,
    problem solving, perception, and language understanding.
    """

    questions = [
        {
            "question": "What is artificial intelligence?",
            "answer_present": True
        },
        {
            "question": "What field does AI belong to?",
            "answer_present": True
        },
        {
            "question": "What type of tasks can AI perform?",
            "answer_present": True
        },
        {
            "question": "Can AI perform learning?",
            "answer_present": True
        },
        {
            "question": "Can AI perform reasoning?",
            "answer_present": True
        },
        {
            "question": "Can AI solve problems?",
            "answer_present": True
        },
        {
            "question": "Can AI understand language?",
            "answer_present": True
        },
        {
            "question": "What does AI create?",
            "answer_present": True
        },
        # Unanswerable questions
        {
            "question": "Who invented artificial intelligence?",
            "answer_present": False
        },
        {
            "question": "What programming language is used for AI?",
            "answer_present": False
        },
    ]

    print("\nContext:")
    print(context)
    print("\n" + "=" * 70)

    for i, item in enumerate(questions, start=1):

        result = qa_pipeline(
            question=item["question"],
            context=context
        )

        print(f"\nQuestion {i}: {item['question']}")
        print(f"Answer: {result['answer']}")
        print(f"Confidence: {result['score']:.4f}")
        print(
            f"Answer Present in Context? "
            f"{'Yes' if item['answer_present'] else 'No'}"
        )

    print("\n" + "=" * 70)
    print("OBSERVATION")
    print("=" * 70)
    print(
        "A standard extractive QA model may still return an answer even "
        "when the correct answer is not present in the context. It is "
        "designed to select the most likely text span rather than always "
        "saying 'I don't know'."
    )
    print(
        "\nThis limitation is important for RAG systems. Even when a "
        "retrieved document does not contain the answer, a model may "
        "produce a misleading response."
    )


if __name__ == "__main__":
    main()