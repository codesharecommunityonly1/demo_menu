import gradio as gr


def hello():
    return "Hello! Menu coming soon."


demo = gr.Interface(fn=hello, inputs=None, outputs="text")
demo.launch()
