import gradio as gr


def view_menu():
    return "Welcome to our Restaurant Menu! 🍽️"


demo = gr.Interface(fn=view_menu, inputs=None, outputs="text")

demo.launch()
