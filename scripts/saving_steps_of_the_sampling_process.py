import os.path

import modules.scripts as scripts
import gradio as gr

from modules import sd_samplers, shared
from modules.processing import Processed, process_images


class Script(scripts.Script):
    def title(self):
        return "Save steps of the sampling process to files"

    def ui(self, is_img2img):
        path = gr.Textbox(label="Save images to path" , value="steps")
        between = gr.Slider(label="between", minimum=1, maximum=10, value=10)
        return [path, between]

    def run(self, p, path, between):
        index = [0]
        dir = os.path.join("outputs",path)
        os.makedirs(dir, exist_ok=True)

        def store_latent(x):
            image = shared.state.current_image = sd_samplers.sample_to_image(x)
            if index[0] % between < 1:
                image.save(os.path.join(dir, f"sample-{index[0]:05}.png"))

            index[0] += 1
            fun(x)

        fun = sd_samplers.store_latent
        sd_samplers.store_latent = store_latent

        try:
            proc = process_images(p)
        finally:
            sd_samplers.store_latent = fun

        return Processed(p, proc.images, p.seed, "")