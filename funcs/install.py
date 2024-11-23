from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich.console import Console
from rich.table import Table
import subprocess
import re
import json
import getpass
import os


def install(package):
    user = getpass.getuser()
    console = Console()
    # comprobar si el paquete existe o no
    # leyendo las keys para buscar el nombre del paquete
    with open(f"/home/{user}/.desktopstudio/keys/main.json", "r") as file:
                data = json.load(file)

    if package in data:
        console.print("[green]Package Founded!")
        # Extraer los valores de "keys" en un array
        keys_array = list(data[package]["keys"].values())
        
        # creamos la tabla para visualizar mejor
        table = Table(title="files to download")

        table.add_column("Url", justify="right", style="cyan", no_wrap=True)
        table.add_column("File", style="magenta")

        for item in keys_array:
              file_name = os.path.basename(item)
              table.add_row(item, file_name)

        console.print(table)
        console.print("Are you sure to continue the install? Y/n")
        confirmation1 = input("[+]")
        if confirmation1 == "":
            confirmation1 = "Y"
        if confirmation1 == "Y":

            os.chdir(f"/home/{user}/.desktopstudio/packages")
            os.mkdir(package)
            os.chdir(f"/home/{user}/.desktopstudio/packages/{package}")

            with Progress(
                TextColumn("[bold blue]{task.description}", justify="right"),
                BarColumn(),
                "[progress.percentage]{task.percentage:>3.1f}%",
                TimeRemainingColumn(),
            ) as progress:

                # Ejecutar una barra de progreso por cada URL en el array
                for url in keys_array:
                    filename = os.path.basename(url)
                    task = progress.add_task(f"Downloading {filename}", total=100)

                    try:
                        # Usar subprocess para ejecutar curl sin mostrar la barra de progreso de curl
                        curl_command = f"curl -# -o {filename} {url}"

                        # Ejecutar el comando curl y leer su salida
                        process = subprocess.Popen(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                        while process.poll() is None:
                            # Leer la salida de stderr (progreso de curl)
                            output = process.stderr.readline()
                            if output:
                                # Buscar el porcentaje de progreso en la salida de `curl`
                                # La salida de `curl` suele ser algo como:  50% [####-----]  ETA 00:00:01
                                match = re.search(r"(\d+)%", output.decode('utf-8'))
                                if match:
                                    percent = int(match.group(1))
                                    progress.update(task, advance=percent - progress.tasks[task].completed)

                        process.wait()  # Esperar a que el proceso termine

                        # Una vez descargado, actualizar la barra al 100%
                        progress.update(task, advance=100)

                    except Exception as e:
                        console.print(f"[red]Error downloading {filename}: {e}[/red]")
             
    else:
        print(f"The key {package} was not found.")

    return