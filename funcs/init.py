from funcs.sysFuncs import getPath
import subprocess
import os
import json

def genConfigFile(path):
    default_config = {
        "general": {
            "path": f"{path}"
        },
        "scripts": {
            "dev": "sudo docker-compose up -d"
        }
    }

    # Guardar la configuración en un archivo JSON
    try:
        with open("DesktopStudio.json", "w") as file:
            json.dump(default_config, file, indent=4)  # `indent=4` para hacerlo legible
    except IOError as e:
        print(f"Error al escribir el archivo: {e}")

def init():
    print("project path (leave blank for the actual path)")
    path = input("[+]")
    if path == "":
        path = getPath()
    print(f"project path selected: {path}")
    print("\nthis project needs a name, write here one")
    projName = input("[+]")
    print(f"{projName}, thats a beautifull name")

    # fin de la configuracion y empezamos a crear directorios
    os.mkdir(f"{path}/{projName}")
    os.chdir(f"{path}/{projName}")

    os.mkdir("mnt")
    # subprocess.run("cp ~/.desktopstudio/defaults/docker-compose.yaml .", shell=True, check=True)
    subprocess.run("cp ~/Desktop/desktop-studio/defaults/docker-compose.yaml .", shell=True, check=True)
    # subprocess.run("cp ~/.desktopstudio/defaults/Dockerfile .", shell=True, check=True)
    subprocess.run("cp ~/Desktop/desktop-studio/defaults/Dockerfile .", shell=True, check=True)
    # subprocess.run("cp ~/.desktopstudio/defaults/supervisord.conf .", shell=True, check=True)
    subprocess.run("cp ~/Desktop/desktop-studio/defaults/supervisord.conf .", shell=True, check=True)
    genConfigFile(f"{path}/{projName}")
    print("config file generated with default values")
    print("you are ready, now run 'DesktopStudio run dev' for the first setup")
    return
    