# Hugging Face Pipeline Benchmark Report

## Objective

The purpose of this benchmark is to compare different Hugging Face Pipeline tasks based on inference time, output quality, hardware usage, and manually evaluated accuracy where applicable.

## Tasks Evaluated

The following tasks were evaluated:

1. Sentiment Analysis
2. Named Entity Recognition
3. Question Answering
4. Text Generation
5. Image Classification
6. Automatic Speech Recognition

## Benchmark Method

For each task:

1. Load the pipeline.
2. Run several test inputs.
3. Measure inference time.
4. Evaluate output quality manually.
5. Compare CPU and GPU performance where practical.

### Timing Formula

```python
import time

start = time.perf_counter()

result = model(input_data)

end = time.perf_counter()

inference_time = end - start
```

## Results Table

| Task                 | Model                  | Hardware | Average Inference Time | Output Quality | Accuracy          |
| -------------------- | ---------------------- | -------- | ---------------------- | -------------- | ----------------- |
| Sentiment Analysis   | Default Pipeline Model | GPU/CPU  | Record Result          | Good           | Record Result     |
| NER                  | Default NER Model      | GPU/CPU  | Record Result          | Good           | Record Result     |
| Question Answering   | Default QA Model       | GPU/CPU  | Record Result          | Good           | Record Result     |
| Text Generation      | DistilGPT-2            | GPU/CPU  | Record Result          | Variable       | Manual Evaluation |
| Image Classification | ViT Base               | GPU/CPU  | Record Result          | Good           | Record Result     |
| Speech Recognition   | Whisper Tiny           | GPU/CPU  | Record Result          | Good           | Manual Evaluation |

## Observations

### Sentiment Analysis

Sentiment analysis is generally fast because the input is short and the model only needs to classify the text into a small number of categories.

### Named Entity Recognition

NER can successfully identify people, organizations, and locations, but performance depends on the training data and entity categories supported by the model.

### Question Answering

Question Answering can provide accurate answers when the answer is available in the context. However, extractive QA models may still return an answer when the context does not contain the correct information.

### Text Generation

Text generation is generally slower than classification tasks because the model generates tokens sequentially. Increasing `max_new_tokens` increases inference time.

### Image Classification

Image classification can produce accurate predictions for common objects but may struggle with unusual images or categories outside the model's training data.

### Speech Recognition

Speech recognition quality depends strongly on audio quality, accent, background noise, and speaking speed.

## CPU vs GPU

A GPU is generally more beneficial for computationally intensive tasks, especially:

* Image classification
* Text generation
* Speech recognition

For very small inputs, the difference may be less noticeable because of model loading and data transfer overhead.

## Conclusion

Hugging Face Pipelines provide a simple and powerful interface for testing multiple AI tasks. They are particularly useful for rapid experimentation and prototyping. However, benchmark results should consider both prediction quality and computational requirements rather than relying only on inference speed.
