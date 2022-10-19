@echo off

set PYTHON=
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS=--xformers --share --gradio-debug --gradio-auth gradio-user:%RANDOM%-%RANDOM%-%RANDOM%
call webui.bat
