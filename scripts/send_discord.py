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
    files = {"file.png":string_img}
    res = requests.post(url, json={}, files=files)
    return res


def send_text_to_discord(url, body):
    res = requests.post(url, json=body)
    return res

class Script(scripts.Script):
    def title(self):
        return "Send discord"

    def ui(self, is_img2img):
        url = gr.Textbox(label="Discord Webhook URL", lines=1)
        return [url]

    def run(self, p, url):
        proc = process_images(p)
        body = {
            "embeds": [{
                "title": p.prompt,
            }]
        }
        print(send_image_to_discord(url, proc.images[0]).status_code)
        print(send_text_to_discord(url, body).status_code)
        # print(send_images_to_discord(url, proc.images).status_code)
        return proc