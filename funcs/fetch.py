from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
import subprocess
import os
import json

def fetch():
    main_keyring_url = ""


    print("WARNING: fetch requests are in BETA, and images can be unstable, continue? Y/n")
    warning = input("[+]")
    if warning == "":
        warning = "Y"
    
    if warning == "Y":
        # proceder
        getKeysTasks = [
            {"description": "Downloading Main Keyring", "func": lambda: subprocess.run(f"temp_file=$(mktemp) && curl -O {main_keyring_url}")},
        ]
    else:
        return