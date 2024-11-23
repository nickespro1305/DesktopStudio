from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich.console import Console
import subprocess
import tempfile
import json

def fetch():
    console = Console()
    main_keyring_url = "https://raw.githubusercontent.com/nickespro1305/DesktopStudio/refs/heads/main/IMAGES/main-keys.json"
    plugins_keyring_url = "https://raw.githubusercontent.com/nickespro1305/DesktopStudio/refs/heads/main/IMAGES/plugins-keys.json"


    print("WARNING: fetch requests are in BETA, and images can be unstable, continue? Y/n")
    warning = input("[+]")
    if warning == "":
        warning = "Y"
    
    if warning == "Y":
        # proceder
        # Crear un archivo temporal para almacenar el JSON
        with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file1, \
            tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file2:
            temp_file_path1 = temp_file1.name
            temp_file_path2 = temp_file2.name
        
        with Progress(
            TextColumn("[bold blue]{task.description}", justify="right"),
            BarColumn(),
            "[progress.percentage]{task.percentage:>3.1f}%",
            TimeRemainingColumn(),
        ) as progress:
            # Descargar el primer archivo
                task_id_1 = progress.add_task("Downloading Main Keyring", total=100)
                try:
                    process1 = subprocess.Popen(
                        f"curl -s {main_keyring_url} -o {temp_file_path1}",
                        shell=True
                    )
                    while process1.poll() is None:
                        progress.update(task_id_1, advance=5)
                        progress.refresh()
                    progress.update(task_id_1, completed=100)
                except Exception as e:
                    console.log(f"[red]Error downloading Keyring 1: {e}")
                    return

                # Descargar el segundo archivo
                task_id_2 = progress.add_task("Downloading Plugins keyring", total=100)
                try:
                    process2 = subprocess.Popen(
                        f"curl -s {plugins_keyring_url} -o {temp_file_path2}",
                        shell=True
                    )
                    while process2.poll() is None:
                        progress.update(task_id_2, advance=5)
                        progress.refresh()
                    progress.update(task_id_2, completed=100)
                except Exception as e:
                    console.log(f"[red]Error downloading Keyring 2: {e}")
                    return
        
        # Leer el JSON descargado
        try:
            with open(temp_file_path1, "r") as file1, open(temp_file_path2, "r") as file2:
                data1 = json.load(file1)
                data2 = json.load(file2)

            # Imprimir los JSON en color
            console.print("")
            console.print("[blue]Keyring 1")
            console.print("")
            console.print_json(json.dumps(data1, indent=2))
            console.print("")
            console.print("[blue]Keyring 2")
            console.print("")
            console.print_json(json.dumps(data2, indent=2))

            # Pedir una ultima confirmacion
            print("Update Keys? Y/n")
            confirmation1 = input("[+]")
            if confirmation1 == "":
                confirmation1 = "Y"
            if confirmation1 == "Y":
                # Descargar los archivos actualizados a las rutas finales
                final_path1 = "~/.desktopstudio/keys/main.json"
                final_path2 = "~/.desktopstudio/keys/plugins.json"

                with Progress(
                    TextColumn("[bold blue]{task.description}", justify="right"),
                    BarColumn(),
                    "[progress.percentage]{task.percentage:>3.1f}%",
                    TimeRemainingColumn(),
                ) as progress:
                    # Descargar el primer archivo actualizado
                    task_id_1 = progress.add_task("Updating Main Keyring", total=100)
                    try:
                        process1 = subprocess.Popen(
                            f"curl -s {main_keyring_url} -o {final_path1}",
                            shell=True
                        )
                        while process1.poll() is None:
                            progress.update(task_id_1, advance=5)
                            progress.refresh()
                        progress.update(task_id_1, completed=100)
                    except Exception as e:
                        console.log(f"[red]Error updating Keyring 1: {e}")

                    # Descargar el segundo archivo actualizado
                    task_id_2 = progress.add_task("Updating Plugins Keyring", total=100)
                    try:
                        process2 = subprocess.Popen(
                            f"curl -s {plugins_keyring_url} -o {final_path2}",
                            shell=True
                        )
                        while process2.poll() is None:
                            progress.update(task_id_2, advance=5)
                            progress.refresh()
                        progress.update(task_id_2, completed=100)
                    except Exception as e:
                        console.log(f"[red]Error updating Keyring 2: {e}")

            else:
                print("[yellow]Operation canceled.")

        except Exception as e:
            console.log(f"[red]Error reading JSON files: {e}")
    else:
        print("[yellow]Operation canceled.")