# Stable Diffusion web UI Patched

## Install

```git
git clone https://github.com/fa0311/stable-diffusion-webui-patched
```

### Option

```git
git clone https://github.com/fa0311/stable-diffusion-webui-patched
git fetch https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
git merge upstream/master
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui-aesthetic-gradients extensions/aesthetic-gradients
```

### What custom scripts?

Check the [custom scripts](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Custom-Scripts) wiki page for extra scripts developed by users.

## Send discord custom scripts

`scripts/send_discord.py`

It is recommended to change `customscript/send_discord.py/txt2img/Discord Webhook URL/value` in [config.json](config.json)

## Video to video with DeepDanbooru custom scripts

`scripts/deep-vid2vid.py`

## Add share.bat

[webui-share.bat](webui-share.bat)

Note that a password is generated each time it is activated, but it is not cryptographically secure.

sample: `--gradio-auth gradio-user:24040-14320-20034`

## Add Config entries (Merged [#3041](https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/3041))

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

## Add xformers message (Merged [#3178](https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/3178))

Added message when installing xformers with unsupported Python versions.
I think this will reduce the amount of confusion people have about installing xformers.

```python
python --version
>>> Python 3.10.8
```

```bat
.\webui-share.bat
>>> Installation of xformers is not supported in this version of Python.
>>> You can also check this and build manually: https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Xformers#building-xformers-on-windows-by-duckness
```

## Fix visible of custom scripts (Discard [#3114](https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/3114))

Fix custom scripts do not reflect visual config.
This is just a minor change with the addition of and inputs[i].visible.
