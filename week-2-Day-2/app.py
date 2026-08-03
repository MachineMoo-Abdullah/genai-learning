import gradio as gr

from auth import authenticate

from callbacks import (
    generate_response,
    clear_fields,
    reset_chat,
    save_chat,
    load_chat
)

from ui.layout import build_layout

history = load_chat()

with gr.Blocks(title="AI Chat Studio") as demo:

    ui = build_layout(history)

    ui["ask_btn"].click(
        fn=generate_response,
        inputs=[
            ui["prompt"],
            ui["history"],
            ui["model"],
        ],
        outputs=[
            ui["chatbot"],
            ui["history"],
        ]
    )

    ui["clear_btn"].click(
        fn=clear_fields,
        outputs=[
            ui["prompt"]
        ]
    )

    ui["reset_btn"].click(
        fn=reset_chat,
        outputs=[
            ui["prompt"],
            ui["chatbot"],
            ui["history"],
        ]
    )

    ui["save_btn"].click(
        fn=save_chat,
        inputs=[
            ui["history"]
        ],
        outputs=[
            ui["status"]
        ]
    )

demo.launch(auth=authenticate)