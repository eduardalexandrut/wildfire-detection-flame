import gradio as gr
import spaces

@spaces.GPU
def detect(image):
    return image

demo = gr.Interface(fn=detect, inputs=gr.Image(), outputs=gr.Image(), title="FLAME-Vision")
demo.launch()