import modules.scripts as scripts
import gradio as gr
from modules.processing import process_images
import requests
from io import BytesIO


def pil_to_byte(img, format="png"):
    img_bytes = BytesIO()
    img.save(img_bytes, format=format)
    img_bytes = img_bytes.getvalue()
    return img_bytes


def send_images_to_discord(url, image_files):
    files = {}
    for key in range(len(image_files)):
        string_img = pil_to_byte(image_files[key], format="png")
        files[f"file{key}.png"] = string_img
    res = requests.post(url, json={}, files=files)
    return res


def send_image_to_discord(url, image_file):
    string_img = pil_to_byte(image_file, format="png")
    files = {"file.png": string_img}
    res = requests.post(url, json={}, files=files)
    return res


def send_text_to_discord(url, body):
    res = requests.post(url, json=body)
    return res


class Script(scripts.Script):
    def title(self):
        return "Send discord"

    def ui(self, is_img2img):
        url = gr.Textbox(label="Discord Webhook URL",placeholder="https://discord.com/api/webhooks/0000000000000000000/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        grid = gr.Checkbox(label="Grid Image Output", value=True)
        all = gr.Checkbox(label="All Image Output")
        embeds = gr.CheckboxGroup(
            label="All Image Output",
            choices=[
                "prompt",
                "negative prompt",
                "seed",
                "sampler",
                "cfg scale",
                "steps",
            ],
            value=["prompt"],
        )
        return [url, grid, all, embeds]

    def run(self, p, url, grid, all, embeds):
        proc = process_images(p)
        fields = []
        if "prompt" in embeds:
            fields.append({"name": "prompt", "value": p.prompt})
        if "negative prompt" in embeds:
            fields.append({"name": "negative prompt", "value": p.negative_prompt})
        if "seed" in embeds:
            fields.append({"name": "seed", "value": str(proc.seed)})
        if "sampler" in embeds:
            fields.append({"name": "sampler", "value": str(proc.sampler)})
        if "cfg scale" in embeds:
            fields.append({"name": "cfg scale", "value": str(p.cfg_scale)})
        if "steps" in embeds:
            fields.append({"name": "steps", "value": str(p.steps)})

        body = {"embeds": [{"fields": fields}]}

        if grid:
            print(send_image_to_discord(url, proc.images[0]).status_code)
        if all and len(proc.images) > 1:
            print(send_images_to_discord(url, proc.images[1:]).status_code)
        if len(fields) > 0:
            print(send_text_to_discord(url, body).status_code)
        return proc
