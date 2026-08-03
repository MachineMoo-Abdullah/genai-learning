import gradio as gr


def create_components(history):

    model_dropdown = gr.Dropdown(
            choices=["Gemini", "Ollama"],
            value="Gemini",
            label="Choose Model"
        )
    
    prompt = gr.Textbox(
        label="Enter Prompt",
        placeholder="Ask anything..."
    )
    chatbot = gr.Chatbot(
        value=history,
        height=500,
        label="AI Chat"
    )

    history_state = gr.State(history)


    ask_btn = gr.Button("Ask AI")

    clear_btn = gr.Button("Clear")

    reset_btn = gr.Button("Reset Chat")

    save_btn = gr.Button("Save Chat")

    status = gr.Textbox(
        label="Status",
        interactive=False
    )

    return {
        "chatbot": chatbot,
        "history": history_state,
        "model": model_dropdown,
        "prompt": prompt,
        "ask_btn": ask_btn,
        "clear_btn": clear_btn,
        "reset_btn": reset_btn,
        "save_btn": save_btn,
        "status": status,
    }