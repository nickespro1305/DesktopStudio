from funcs.interactiveFuncs import *
from funcs.sysFuncs import get_folders_in_directory
from rich.console import Console
import getpass
import subprocess

def remove_package(folder):
    subprocess.run(f"rm -r {folder}", shell=True)
    return


def rm(package):
    console = Console()
    user = getpass.getuser()
    plugins = get_folders_in_directory(f"/home/{user}/.desktopstudio/plugins")
    flavours = get_folders_in_directory(f"/home/{user}/.desktopstudio/packages")

    if package in plugins:
        confirmation1 = confirmation(f"[blue]are you sure to[/blue] [bold red]remove {package}[/bold red][blue]?[/blue]  [green]Y[/green]/[red]n[/red]", "[purple]$", 1)
        if confirmation1 == "Y":
            remove_package(f"/home/{user}/.desktopstudio/plugins/{package}")

    if package in flavours:
        confirmation1 = confirmation(f"[blue]are you sure to[/blue] [bold red]remove {package}[/bold red][blue]?[/blue]  [green]Y[/green]/[red]n[/red]", "[purple]$", 1)
        if confirmation1 == "Y":
            remove_package(f"/home/{user}/.desktopstudio/packages/{package}")

    return