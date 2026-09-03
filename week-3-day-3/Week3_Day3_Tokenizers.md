# Week 3 – Day 3: LLM Tokenizers

## Objective

Understand the transformation that happens between human-readable text and the numerical representation processed by an LLM:

```text
Human Text
    ↓
Tokenizer
    ↓
Token IDs
    ↓
LLM
    ↓
Token IDs
    ↓
Tokenizer
    ↓
Human Text
```

A tokenizer is therefore the interface between human language and the model's numerical input/output space.

---

## 1. What is a tokenizer?

A tokenizer is software that converts text into smaller units called **tokens** and maps those tokens to integers called **token IDs**.

A token is not necessarily a whole word. Depending on the tokenizer, a token may be:

- a complete word,
- part of a word,
- punctuation,
- whitespace plus text,
- a number or part of a number,
- a byte/character-like unit,
- or a special control marker.

For example, a tokenizer might split:

```text
Generative
```

into pieces similar to:

```text
Gener + ative
```

Another tokenizer may represent the same word with one token or several different subword pieces.

---

## 2. Why can't an LLM directly understand text?

Neural networks operate on numbers, not raw strings.

The transformer receives vectors. Before text reaches the transformer:

1. the tokenizer maps text to token IDs;
2. each token ID selects an embedding vector;
3. the transformer processes those vectors.

So the model does not receive the Python string `"Hello"` directly. It receives numerical IDs that are then converted to learned embeddings.

---

## 3. What is encoding?

**Encoding** is the conversion:

```text
Text → Token IDs
```

In Hugging Face:

```python
token_ids = tokenizer.encode(text)
```

Example conceptually:

```text
"Hello world"
       ↓
[9906, 1917]
```

The actual IDs depend on the tokenizer.

---

## 4. What is decoding?

**Decoding** performs the reverse mapping:

```text
Token IDs → Text
```

In Hugging Face:

```python
text = tokenizer.decode(token_ids)
```

For normal text, encoding followed by decoding often reconstructs the original string. Exact equality is not guaranteed in every configuration because tokenizers may normalize whitespace, handle special tokens, or apply other transformations.

---

## 5. What is a token ID?

A token ID is the integer index assigned to a token in the tokenizer's vocabulary.

Example:

```text
Token       ID
"Hello"     1234
" world"    5678
```

The LLM's embedding table uses the integer ID to select a learned vector.

The same integer does **not** necessarily mean the same token across different model families.

---

## 6. What are special tokens?

Special tokens are control tokens that communicate structure rather than ordinary user text.

Examples can include:

- beginning of sequence,
- end of sequence,
- padding,
- unknown token,
- user-role markers,
- assistant-role markers,
- system-role markers,
- tool-call markers.

Each model family defines its own conventions.

### BOS

**BOS** means **Beginning Of Sequence**. It can mark the start of a sequence.

Not every tokenizer inserts BOS automatically, and not every chat format uses it in the same way.

### EOS

**EOS** means **End Of Sequence**. It can signal that a sequence or assistant response is finished.

EOS behavior is important during generation because it can be used as a stopping condition.

### PAD

A **padding token** is used to make sequences in the same batch reach compatible lengths.

### UNK

An **unknown token** represents content that cannot be represented directly by a tokenizer. Modern byte-aware tokenizers may rarely need a traditional UNK token for ordinary text.

---

## 7. What is a chat template?

A chat model normally expects messages to be serialized into a specific text/token format.

A program may represent a conversation as:

```python
messages = [
    {"role": "system", "content": "You are helpful."},
    {"role": "user", "content": "Explain recursion."},
]
```

But the model cannot consume this Python list directly.

The tokenizer's **chat template** transforms these structured messages into the model's expected sequence of role markers, text, separators, and special tokens.

With Hugging Face:

```python
tokenizer.apply_chat_template(messages)
```

The exact rendering differs between models.

---

## 8. Why are chat templates necessary?

Instruction-tuned models learn a particular conversation format during training or alignment.

The template tells the model:

- which text is a system instruction,
- which text came from the user,
- which text belongs to the assistant,
- where turns begin/end,
- where the model should start generating,
- and sometimes where tool calls/results belong.

Using the wrong template can make the model misunderstand speaker roles, ignore system instructions, continue the wrong speaker, generate unnecessary control text, or stop incorrectly.

---

## 9. Why do different LLMs tokenize the same sentence differently?

Different tokenizers may use:

- different vocabulary sizes,
- different training corpora,
- different subword algorithms,
- different normalization rules,
- different handling of spaces,
- different treatment of punctuation/numbers/code,
- different multilingual coverage,
- different special-token conventions.

Their vocabularies are learned or designed independently.

Therefore:

```text
Exactly the same sentence
```

can map to different token pieces and different token counts.

---

## 10. Why can two models receive exactly the same sentence but get a different number of tokens?

A tokenizer has a fixed vocabulary of reusable pieces.

Suppose Tokenizer A contains:

```text
"artificial"
" intelligence"
```

as two common pieces.

Tokenizer B might contain pieces closer to:

```text
"art"
"ificial"
" int"
"elligence"
```

The visible sentence is identical, but the internal segmentation is not.

Therefore token count depends on the tokenizer, not only on the number of human-readable words or characters.

---

## 11. Why does tokenization affect the context window?

Context windows are usually measured in **tokens**, not words.

If a model has a 16,384-token context window, then:

```text
prompt tokens + conversation history + generated tokens
```

must fit within the deployment's supported context budget.

A tokenizer that represents a particular document in more tokens consumes the context budget faster for that document.

Important: a larger advertised model context window and a more compact tokenizer are separate concepts.

---

## 12. Why does tokenization affect API cost?

Many LLM APIs charge according to input and output token counts.

Conceptually:

```text
input_cost =
    input_tokens / 1,000,000 × price_per_million_input_tokens
```

Therefore the tokenizer used by the served model directly affects metered token counts.

Always use the provider/model's actual tokenizer and current pricing rather than estimating from word count.

---

## 13. Why does tokenization affect inference speed?

More input tokens generally mean more positions the model must process.

This can increase:

- prompt-processing work,
- memory use,
- latency,
- attention/KV-cache requirements.

However, tokenizer efficiency is only one factor. Architecture, hardware, batching, attention implementation, quantization, and serving software can matter far more.

---

## 14. Why does tokenization affect multilingual text?

Tokenizer vocabularies reflect their training/design data.

If a language, script, or character pattern has good vocabulary coverage, common words may be represented compactly.

If coverage is weaker, the tokenizer may split text into more pieces.

This is why equivalent sentences in English, Urdu, Arabic, and Chinese can have very different token counts.

A four-sentence classroom experiment is **not** enough to conclude that one tokenizer is universally best for an entire language.

---

## 15. Trade-offs: are fewer tokens always better?

No.

A tokenizer producing fewer tokens on one benchmark may be attractive for context efficiency, but tokenizer quality involves trade-offs:

- vocabulary size,
- multilingual coverage,
- code representation,
- handling of rare words,
- compatibility with model training,
- embedding/output-layer size,
- segmentation quality,
- latency and memory behavior.

The correct tokenizer for a pretrained model is the tokenizer the model was trained to use. Swapping in another tokenizer simply because it produces fewer tokens usually breaks the token-to-embedding mapping.

---

## 16. Key practical lesson

Never think of an LLM prompt as only a string.

Think of it as:

```text
Text
→ tokenizer-specific segmentation
→ tokenizer-specific integer IDs
→ embeddings
→ transformer computation
```

And for chat models:

```text
Messages
→ model-specific chat template
→ special/control markers
→ token IDs
→ LLM
```

That is why tokenizer inspection is an essential debugging skill for LLM applications.
