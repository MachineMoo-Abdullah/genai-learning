from callbacks import load_chat
from ui.layout import create_layout

history = load_chat()

demo = create_layout(history)

demo.launch()