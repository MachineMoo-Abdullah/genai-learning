import gradio as gr

from ui.components import create_components
from callbacks import (
    generate_response,
    clear_chat,
    reset_chat,
    save_chat
)


def create_layout(history):

    with gr.Blocks(title="AI Assistant") as demo:

        gr.Markdown("# 🤖 AI Assistant")

        c = create_components(history)
        inputs1=[

            c["prompt"],
            c["history"],
            c["assistant"],
            c["model"],
            c["template"],
            c["document"]

        ]
        c["ask_btn"].click(
            fn=generate_response,
            inputs=inputs1,
            outputs=[
                c["chatbot"],
                c["history"]
            ]
        )

        c["prompt"].submit(
            fn=generate_response,
            inputs=inputs1,
            outputs=[
                c["chatbot"],
                c["history"]
            ]
        )

        c["clear_btn"].click(
            fn=clear_chat,
            outputs=c["prompt"]
        )

        c["reset_btn"].click(
            fn=reset_chat,
            outputs=[
                c["chatbot"],
                c["history"],
                c["status"]
            ]
        )

        c["save_btn"].click(
            fn=save_chat,
            inputs=c["history"],
            outputs=c["status"]
        )

    return demo