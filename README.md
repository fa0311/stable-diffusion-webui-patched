# Stable Diffusion web UI Patched

## Send discord

[scripts/send_discord.py](scripts/send_discord.py)

It is recommended to change `customscript/send_discord.py/txt2img/Discord Webhook URL/value` in [config.json](config.json)

## Installation and Running

Make sure the required [dependencies](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Dependencies) are met and follow the instructions available for both [NVidia](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and-Run-on-NVidia-GPUs) (recommended) and [AMD](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and-Run-on-AMD-GPUs) GPUs.

Alternatively, use Google Colab:

- [Colab, maintained by Akaibu](https://colab.research.google.com/drive/1kw3egmSn-KgWsikYvOMjJkVDsPLjEMzl)
- [Colab, original by me, outdated](https://colab.research.google.com/drive/1Iy-xW9t1-OQWhb0hNxueGij8phCyluOh).

Note that a password is generated each time it is activated, but it is not cryptographically secure.

sample: `--gradio-auth gradio-user:24040-14320-20034`

## Add Config entries (Merged)

Script added to ui-config.json.

```ui-config.json
{
    "txt2img/Script/value": "Prompt matrix",
    "img2img/Script/value": "None"
}
```

Dropdown visibility added to ui-config.json.

```ui-config.json
{
    "txt2img/Style 1/visible": true,
    "txt2img/Style 2/visible": true,
    "txt2img/Script/visible": true,
    "img2img/Style 1/visible": true,
    "img2img/Style 2/visible": true,
    "img2img/Script/visible": true
}
```
