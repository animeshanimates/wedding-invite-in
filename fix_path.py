import os

filepath = 'script_main.BNG1a6lE.mjs'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("path:`/demos/laavan`", "path:`/wedding-invite-in/`")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)
