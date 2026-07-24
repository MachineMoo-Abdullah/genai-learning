1. What is Ollama?

Ollama is a tool that lets you download, run, and manage Large Language Models (LLMs) on your own computer. It provides a simple command-line interface and API to interact with models like Llama, Mistral, Gemma, and Qwen.

2. Why use local LLMs?

People use local LLMs because they:

Keep data private (no need to send it to the internet).
Work even without an internet connection.
Have no API usage costs.
Allow full control over the model and its settings.

3. Difference between Local and Cloud LLMs

| Local LLM                 | Cloud LLM                    |
| ------------------------- | ---------------------------- |
| Runs on your own computer | Runs on remote servers       |
| Better privacy            | Data is sent to the provider |
| Works offline             | Requires internet            |
| No per-request cost       | Usually charges per API call |
| Depends on your hardware  | Uses powerful cloud GPUs     |


4. What is an Open-Source Model?

An open-source model is an AI model whose weights and code are publicly available, allowing anyone to download, use, and sometimes modify it according to its license.

5. Explain Different Models

- Llama
Developed by Meta.
General-purpose language model.
Good balance of performance and efficiency.

- Qwen
Developed by Alibaba.
Strong at coding, reasoning, and multilingual tasks.
Performs well on many benchmarks.

- Mistral
Developed by Mistral AI.
Lightweight and fast.
Good choice for local deployment.

- Gemma
Developed by Google.
Smaller, efficient models.
Designed for research and local AI applications.

6. What are Model Parameters (7B, 14B, 70B)?

Parameters are the learned weights inside a model.

7B = 7 billion parameters
14B = 14 billion parameters
70B = 70 billion parameters

Generally:

More parameters → Better understanding and reasoning.
More parameters → Higher RAM/VRAM requirements and slower inference.

 7. How do RAM, VRAM, and Model Size Affect Performance?

RAM: Stores the model when running on the CPU.
VRAM: GPU memory used when running on the GPU. More VRAM usually means faster inference.
Model Size: Larger models need more RAM/VRAM and take longer to load but often produce better results.

8. Advantages of Running LLMs Locally

Better privacy and security.
Works without internet.
No API usage costs.
Faster responses after the model is loaded.
Full control over the model.

9. Disadvantages of Running LLMs Locally

Requires powerful hardware.
Large models consume significant RAM/VRAM.
Initial model download can be large.
Performance may be slower than high-end cloud servers.
You are responsible for updates and maintenance.