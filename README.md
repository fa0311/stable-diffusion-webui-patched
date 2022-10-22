# Stable Diffusion web UI Patched

## Send discord

Check the [custom scripts](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Custom-Scripts) wiki page for extra scripts developed by users.

It is recommended to change `customscript/send_discord.py/txt2img/Discord Webhook URL/value` in [config.json](config.json)

## Add share.bat

[webui-share.bat](webui-share.bat)

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
