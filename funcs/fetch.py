from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich.console import Console
import subprocess
import tempfile
import json

def fetch():
    console = Console()
    main_keyring_url = "https://raw.githubusercontent.com/nickespro1305/DesktopStudio/refs/heads/main/IMAGES/main-keys.json"


    print("WARNING: fetch requests are in BETA, and images can be unstable, continue? Y/n")
    warning = input("[+]")
    if warning == "":
        warning = "Y"
    
    if warning == "Y":
        # proceder
        # Crear un archivo temporal para almacenar el JSON
        with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
            temp_file_path = temp_file.name
        
        with Progress(
            TextColumn("[bold blue]{task.description}", justify="right"),
            BarColumn(),
            "[progress.percentage]{task.percentage:>3.1f}%",
            TimeRemainingColumn(),
        ) as progress:
            task_id = progress.add_task("Downloading Main Keyring", total=100)
            
            try:
                # Iniciar el comando curl y actualizar la barra mientras se descarga
                process = subprocess.Popen(
                    f"curl -s {main_keyring_url} -o {temp_file_path}",
                    shell=True
                )
                
                # Simular progreso mientras `curl` se ejecuta
                while process.poll() is None:
                    progress.update(task_id, advance=5)
                    progress.refresh()
                
                progress.update(task_id, completed=100)  # Completar la barra al finalizar
            except Exception as e:
                console.log(f"[red]Error during download: {e}")
                return
        
        # Leer el JSON descargado
        try:
            with open(temp_file_path, "r") as file:
                data = json.load(file)
            
            # Imprimir el JSON en color
            console.print("")
            console.print("[blue]Main Keyring")
            console.print("")
            console.print_json(json.dumps(data, indent=2))

            # Pedir una ultima confirmacion
            print("Update Keys? Y/n")
            confirmation1 = input("[+]")
            if confirmation1 == "":
                confirmation1 = "Y"
            if confirmation1 == "Y":
                # descargar el nuevo keyring

                with Progress(
                    TextColumn("[bold blue]{task.description}", justify="right"),
                    BarColumn(),
                    "[progress.percentage]{task.percentage:>3.1f}%",
                    TimeRemainingColumn(),
                ) as progress:
                    task_id = progress.add_task("Downloading Main Keyring", total=100)
            
                    try:
                        # Iniciar el comando curl y actualizar la barra mientras se descarga
                        process = subprocess.Popen(
                            f"curl -s {main_keyring_url} -o ~/.desktopstudio/keys/main.json",
                            shell=True
                        )
                
                        # Simular progreso mientras `curl` se ejecuta
                        while process.poll() is None:
                            progress.update(task_id, advance=5)
                            progress.refresh()
                
                        progress.update(task_id, completed=100)  # Completar la barra al finalizar
                    except Exception as e:
                        console.log(f"[red]Error during download: {e}")
                return
            else:
                print("[yellow]Operation canceled.")

        except Exception as e:
            console.log(f"[red]Error reading JSON file: {e}")
    else:
        print("[yellow]Operation canceled.")