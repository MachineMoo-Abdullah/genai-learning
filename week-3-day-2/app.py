import gradio as gr
import torch
from transformers import pipeline


# ============================================================
# DEVICE CONFIGURATION
# ============================================================

DEVICE = 0 if torch.cuda.is_available() else -1

print(f"Using device: {'GPU' if DEVICE == 0 else 'CPU'}")


# ============================================================
# LOAD PIPELINES
# ============================================================
# For a student project, loading pipelines once makes the app
# easier to use. On low-memory systems, you can use lazy loading.
# ============================================================

sentiment_pipeline = None
ner_pipeline = None
qa_pipeline = None
generation_pipeline = None
image_pipeline = None
speech_pipeline = None


def get_sentiment_pipeline():
    global sentiment_pipeline

    if sentiment_pipeline is None:
        sentiment_pipeline = pipeline(
            "sentiment-analysis",
            device=DEVICE
        )

    return sentiment_pipeline


def get_ner_pipeline():
    global ner_pipeline

    if ner_pipeline is None:
        ner_pipeline = pipeline(
            "ner",
            aggregation_strategy="simple",
            device=DEVICE
        )

    return ner_pipeline


def get_qa_pipeline():
    global qa_pipeline

    if qa_pipeline is None:
        qa_pipeline = pipeline(
            "question-answering",
            device=DEVICE
        )

    return qa_pipeline


def get_generation_pipeline():
    global generation_pipeline

    if generation_pipeline is None:
        generation_pipeline = pipeline(
            "text-generation",
            model="distilgpt2",
            device=DEVICE
        )

    return generation_pipeline


def get_image_pipeline():
    global image_pipeline

    if image_pipeline is None:
        image_pipeline = pipeline(
            "image-classification",
            model="google/vit-base-patch16-224",
            device=DEVICE
        )

    return image_pipeline


def get_speech_pipeline():
    global speech_pipeline

    if speech_pipeline is None:
        speech_pipeline = pipeline(
            "automatic-speech-recognition",
            model="openai/whisper-tiny",
            device=DEVICE
        )

    return speech_pipeline


# ============================================================
# SENTIMENT ANALYSIS
# ============================================================

def analyze_sentiment(text):

    if not text.strip():
        return "Please enter some text."

    classifier = get_sentiment_pipeline()
    result = classifier(text)[0]

    return (
        f"Predicted Sentiment: {result['label']}\n"
        f"Confidence: {result['score']:.4f}"
    )


# ============================================================
# NAMED ENTITY RECOGNITION
# ============================================================

def analyze_ner(text):

    if not text or not text.strip():
        return {"message": "Please enter some text.", "entities": []}

    ner_model = get_ner_pipeline()
    entities = ner_model(text)

    if not entities:
        return {"message": "No entities were detected.", "entities": []}

    output = []

    for entity in entities:
        output.append({
            "Entity": entity["word"],
            "Type": entity["entity_group"],
            "Confidence": round(float(entity["score"]), 4)
        })

    return {
        "message": f"{len(output)} entities detected.",
        "entities": output
    }


# ============================================================
# QUESTION ANSWERING
# ============================================================

def answer_question(question, context):

    if not question.strip() or not context.strip():
        return "Please provide both a question and context."

    qa_model = get_qa_pipeline()

    result = qa_model(
        question=question,
        context=context
    )

    return (
        f"Answer: {result['answer']}\n"
        f"Confidence: {result['score']:.4f}"
    )


# ============================================================
# TEXT GENERATION
# ============================================================

def generate_text(prompt, max_tokens, temperature, do_sample):

    if not prompt.strip():
        return "Please enter a prompt."

    generator = get_generation_pipeline()

    kwargs = {
        "max_new_tokens": int(max_tokens),
        "do_sample": do_sample
    }

    # Temperature only applies when sampling
    if do_sample:
        kwargs["temperature"] = float(temperature)

    result = generator(
        prompt,
        **kwargs
    )

    return result[0]["generated_text"]


# ============================================================
# IMAGE CLASSIFICATION
# ============================================================

def classify_image(image):

    if image is None:
        return {}

    classifier = get_image_pipeline()

    predictions = classifier(
        image,
        top_k=5
    )

    return {
        prediction["label"]: float(prediction["score"])
        for prediction in predictions
    }


# ============================================================
# SPEECH TO TEXT
# ============================================================

def speech_to_text(audio):

    if audio is None:
        return "Please upload or record an audio file."

    transcriber = get_speech_pipeline()

    result = transcriber(audio)

    return result["text"]


# ============================================================
# GRADIO INTERFACE
# ============================================================

with gr.Blocks(
    title="Hugging Face Multi-Task AI Playground"
) as app:

    gr.Markdown(
        """
        # 🤗 Hugging Face Multi-Task AI Playground

        Explore multiple Artificial Intelligence tasks using
        Hugging Face Transformers Pipelines.

        Select a tab and provide your input!
        """
    )

    # --------------------------------------------------------
    # TAB 1: SENTIMENT
    # --------------------------------------------------------

    with gr.Tab("😊 Sentiment Analysis"):

        sentiment_input = gr.Textbox(
            label="Enter Text",
            placeholder="I really enjoyed this product!"
        )

        sentiment_button = gr.Button("Analyze Sentiment")

        sentiment_output = gr.Textbox(
            label="Result"
        )

        sentiment_button.click(
            analyze_sentiment,
            inputs=sentiment_input,
            outputs=sentiment_output
        )

    # --------------------------------------------------------
    # TAB 2: NER
    # --------------------------------------------------------

    with gr.Tab("🏷️ Named Entity Recognition"):

        ner_input = gr.Textbox(
            label="Enter Text",
            lines=5,
            placeholder="Microsoft opened a new office in London."
        )

        ner_button = gr.Button("Extract Entities")

        ner_output = gr.JSON(
            label="Detected Entities"
        )

        ner_button.click(
            analyze_ner,
            inputs=ner_input,
            outputs=ner_output
        )

    # --------------------------------------------------------
    # TAB 3: QUESTION ANSWERING
    # --------------------------------------------------------

    with gr.Tab("❓ Question Answering"):

        qa_context = gr.Textbox(
            label="Context",
            lines=6,
            value=(
                "Artificial intelligence is a field of computer science "
                "focused on creating systems capable of performing tasks "
                "that normally require human intelligence."
            )
        )

        qa_question = gr.Textbox(
            label="Question",
            placeholder="What is artificial intelligence?"
        )

        qa_button = gr.Button("Get Answer")

        qa_output = gr.Textbox(
            label="Answer"
        )

        qa_button.click(
            answer_question,
            inputs=[qa_question, qa_context],
            outputs=qa_output
        )

    # --------------------------------------------------------
    # TAB 4: TEXT GENERATION
    # --------------------------------------------------------

    with gr.Tab("✍️ Text Generation"):

        generation_prompt = gr.Textbox(
            label="Prompt",
            lines=3,
            value="Write a short product description for an AI receptionist:"
        )

        max_tokens = gr.Slider(
            minimum=10,
            maximum=150,
            value=60,
            step=10,
            label="Maximum New Tokens"
        )

        temperature = gr.Slider(
            minimum=0.1,
            maximum=1.5,
            value=0.7,
            step=0.1,
            label="Temperature"
        )

        do_sample = gr.Checkbox(
            value=True,
            label="Enable Sampling"
        )

        generation_button = gr.Button("Generate")

        generation_output = gr.Textbox(
            label="Generated Text",
            lines=8
        )

        generation_button.click(
            generate_text,
            inputs=[
                generation_prompt,
                max_tokens,
                temperature,
                do_sample
            ],
            outputs=generation_output
        )

    # --------------------------------------------------------
    # TAB 5: IMAGE CLASSIFICATION
    # --------------------------------------------------------

    with gr.Tab("🖼️ Image Classification"):

        image_input = gr.Image(
            type="pil",
            label="Upload an Image"
        )

        image_button = gr.Button("Classify Image")

        image_output = gr.Label(
            num_top_classes=5,
            label="Predictions"
        )

        image_button.click(
            classify_image,
            inputs=image_input,
            outputs=image_output
        )

    # --------------------------------------------------------
    # TAB 6: SPEECH TO TEXT
    # --------------------------------------------------------

    with gr.Tab("🎤 Speech to Text"):

        audio_input = gr.Audio(
            type="filepath",
            label="Upload or Record Audio"
        )

        audio_button = gr.Button("Transcribe Audio")

        audio_output = gr.Textbox(
            label="Transcription",
            lines=5
        )

        audio_button.click(
            speech_to_text,
            inputs=audio_input,
            outputs=audio_output
        )


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":
    app.launch()