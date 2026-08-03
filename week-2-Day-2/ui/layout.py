import gradio as gr

from ui.components import create_components


def build_layout(history):

    gr.Markdown("# 🤖 AI Chat Studio")

    components = create_components(history)

    components["model"]

    components["chatbot"]

    components["prompt"]

    with gr.Row():

        components["ask_btn"]

        components["clear_btn"]

        components["reset_btn"]

        components["save_btn"]

    components["status"]

    return components