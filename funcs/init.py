from funcs.sysFuncs import getPath, get_folders_in_directory
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich.console import Console
import subprocess
import os
import json
import getpass

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
    user = getpass.getuser()
    console = Console()

    print("project path (leave blank for the actual path)")
    path = input("[+]")
    if path == "":
        path = getPath()
    print(f"project path selected: {path}")

    print("\nthis project needs a name, write here one")
    projName = input("[+]")
    print(f"{projName}, thats a beautifull name")

    packages = get_folders_in_directory(f"/home/{user}/.desktopstudio/packages")
    console.print(f"Flavours: {packages}")
    flavour = input("[+]")
    
    tasks = [
        {"description": "Generate project folder", "func": lambda: os.mkdir(f"{projName}")},
        {"description": "Moving into the project folder", "func": lambda: os.chdir(f"{projName}")},
        {"description": "Create mnt folder", "func": lambda: os.mkdir("mnt")},
        {"description": "Copy docker-compose.yaml", "func": lambda: subprocess.run(f"cp ~/.desktopstudio/packages/{flavour}/docker-compose.yaml .", shell=True, check=True)},
        {"description": "Copy Dockerfile", "func": lambda: subprocess.run(f"cp ~/.desktopstudio/packages/{flavour}/Dockerfile .", shell=True, check=True)},
        {"description": "Copy supervysor conf file", "func": lambda: subprocess.run(f"cp ~/.desktopstudio/packages/{flavour}/supervisord.conf .", shell=True, check=True)},
        {"description": "Generate config file", "func": lambda: genConfigFile(f"{path}/{projName}")},
    ]

    with Progress(
        TextColumn("[bold blue]{task.description}", justify="right"),  # Accedemos directamente a 'description'
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.1f}%",
        TimeRemainingColumn(),
    ) as progress:
        # Crear las tareas con descripción explícita
        task_ids = {
            task["description"]: progress.add_task(
                description=task["description"], total=1
            )
            for task in tasks
        }

        # Ejecutar cada tarea y actualizar su barra correspondiente
        for task in tasks:
            try:
                task["func"]()
                progress.update(task_ids[task["description"]], advance=1)
            except Exception as e:
                progress.console.log(f"[red]Error during {task['description']}: {e}")
                return