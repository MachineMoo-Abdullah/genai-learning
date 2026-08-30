# Week 3 – Day 2: Hugging Face Pipelines

## Objective

The objective of this project is to build a multi-task AI application using Hugging Face Pipelines. The application supports multiple artificial intelligence tasks, including text analysis, question answering, text generation, image classification, and speech recognition.

The general workflow is:

**Hugging Face Model → Pipeline → Input → AI Output**

A pipeline provides a simple interface for using pretrained models without manually handling all of the underlying components.

---

## What is a Hugging Face Pipeline?

A Hugging Face Pipeline is a high-level API provided by the Transformers library that makes it easy to use pretrained machine learning models.

For example:

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("I love artificial intelligence!")
```

The pipeline automatically performs the necessary preprocessing, model inference, and output processing.

---

## Why use `pipeline()` instead of manually loading a tokenizer and model?

When using the lower-level Transformers API, developers usually need to manually:

1. Load a tokenizer.
2. Load a pretrained model.
3. Convert the input into tokens.
4. Pass the tokens to the model.
5. Process the model output.
6. Convert predictions into a human-readable format.

A pipeline performs these steps automatically. Therefore, it is faster and easier for experimentation and prototyping.

---

## What happens internally when a pipeline is created?

When a pipeline is created, Hugging Face generally:

1. Selects a suitable model for the requested task.
2. Downloads the model checkpoint if it is not already available.
3. Loads the tokenizer or feature extractor.
4. Loads the trained model weights.
5. Prepares preprocessing and postprocessing functions.
6. Runs inference when input is provided.

The overall process is:

**Input → Preprocessing → Model → Postprocessing → Output**

---

## What is Inference?

Inference is the process of using an already trained machine learning model to make predictions on new data.

For example, after a sentiment analysis model has been trained, we can give it a new review and ask whether the sentiment is positive or negative. This prediction process is called inference.

Training teaches a model, while inference uses the trained model.

---

## What is a Model Checkpoint?

A model checkpoint is a saved version of a trained model. It usually contains the learned model parameters and configuration needed to reuse the model.

Pretrained models on the Hugging Face Hub are commonly distributed as checkpoints.

For example, a checkpoint may contain the knowledge learned by a language model during training and can be downloaded later for inference or fine-tuning.

---

## What is Named Entity Recognition (NER)?

Named Entity Recognition is a Natural Language Processing task that identifies important entities in text and classifies them into categories.

Examples include:

* **PER** — Person
* **ORG** — Organization
* **LOC** — Location
* **DATE** — Date

For example:

> "Microsoft opened an office in London."

An NER model may identify:

* Microsoft → Organization
* London → Location

---

## What is Sentiment Analysis?

Sentiment analysis determines the emotional opinion or attitude expressed in text.

Typical categories include:

* Positive
* Negative
* Neutral

For example:

> "This product is amazing!" → Positive

> "I am disappointed with the service." → Negative

---

## What is Question Answering?

Question Answering is an NLP task where a model answers a question based on provided information.

For extractive question answering, the model usually finds an answer directly from a given context.

For example:

**Context:** Artificial intelligence is a field of computer science.

**Question:** What field does AI belong to?

**Answer:** Computer science

---

## What is Text Generation?

Text generation involves using a language model to generate new text based on an input prompt.

For example:

**Prompt:** Write a description of an AI receptionist.

The model may generate text describing its features and capabilities.

Generation quality and creativity can be controlled using parameters such as `max_new_tokens`, `temperature`, and `do_sample`.

---

## What is Image Classification?

Image classification is a computer vision task where a model analyzes an image and predicts the category or object represented in that image.

For example:

**Image:** Photograph of a dog

**Prediction:** Golden Retriever

The model usually returns predicted labels along with confidence scores.

---

## What is Automatic Speech Recognition?

Automatic Speech Recognition (ASR), also called Speech-to-Text, converts spoken audio into written text.

The workflow is:

**Audio → Speech Recognition Model → Text**

ASR models may make errors because of:

* Background noise
* Different accents
* Fast speech
* Poor audio quality

---

## When should you use a Pipeline?

Pipelines are useful when:

* You want to quickly test a pretrained model.
* You are learning Hugging Face.
* You want to build a prototype.
* You do not need extensive customization.
* You want simple preprocessing and postprocessing.

---

## When should you use the lower-level Transformers API?

The lower-level API is better when:

* You need a specific model or tokenizer configuration.
* You want to fine-tune a model.
* You need custom preprocessing.
* You want access to raw model outputs.
* You are optimizing a production system.

### Conclusion

Pipelines are excellent for quickly using pretrained models, while the lower-level Transformers API provides more control and flexibility.
