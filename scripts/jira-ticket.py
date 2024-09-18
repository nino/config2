#!/usr/bin/env python
import subprocess

clipboard_content = subprocess.check_output(["pbpaste"]).decode("utf-8").split("\n")

title = clipboard_content[0]
url = clipboard_content[1]
id = url.split("/")[-1]

print(f"[{id} {title}]({url})")
