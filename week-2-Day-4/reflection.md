# Reflection

## 1. Why did Transformers replace LSTMs?

Transformers use **self-attention**, allowing them to process many tokens in parallel. They train faster, handle long-range relationships better, and scale more effectively than LSTMs.

## 2. Why do larger models usually require more hardware?

Larger models have more **parameters**, which require more memory, storage, and computing power. Therefore, they often need more GPUs or specialized hardware.

## 3. Why doesn't a model remember previous chats forever?

Models have a limited **context window**. Old conversations may be removed or summarized when the context becomes too large.

## 4. How does tokenization affect API cost?

APIs usually charge based on **tokens processed**. More tokens mean higher API usage and cost.

## 5. If you were designing an LLM, what improvements would you make?

I would focus on **better reasoning, lower computational cost, longer context, better accuracy, stronger memory, and multimodal capabilities**.
