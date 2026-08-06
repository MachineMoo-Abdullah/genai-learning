import gradio as gr


def create_components(history):

    model_dropdown = gr.Dropdown(
        choices=["Gemini", "Ollama"],
        value="Gemini",
        label="Choose Model"
    )

    assistant_dropdown = gr.Dropdown(
        choices=[
            "Software Engineer",
            "QA Engineer",
            "Career Mentor",
            "Technical Trainer"
        ],
        value="Software Engineer",
        label="Choose Assistant"
    )
    template_dropdown = gr.Dropdown(

        choices=[
            "Normal",
            "Code Review",
            "Bug Fix",
            "Documentation"
        ],

        value="Normal",

        label="Prompt Template"
    )

    prompt = gr.Textbox(
        label="Enter Prompt",
        placeholder="Ask anything..."
    )
    document = gr.File(

        label="Upload TXT or PDF",

        file_types=[".txt", ".pdf"]
    )

    chatbot = gr.Chatbot(
        value=history,
        height=500,
        label="AI Chat"
    )

    history_state = gr.State(history)

    ask_btn = gr.Button("Ask AI", variant="primary")

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
        "assistant": assistant_dropdown,
        "template": template_dropdown,
        "prompt": prompt,
        "document": document,
        "ask_btn": ask_btn,
        "clear_btn": clear_btn,
        "reset_btn": reset_btn,
        "save_btn": save_btn,
        "status": status,
    }