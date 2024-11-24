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
        console.print(f"are you sure to remove {package}?  Y/n")
        confirmation1 = input("[+]")
        if confirmation1 == "":
            confirmation1 = "Y"
        if confirmation1 == "Y":
            remove_package(f"/home/{user}/.desktopstudio/plugins/{package}")

    if package in flavours:
        console.print(f"are you sure to remove {package}?  Y/n")
        confirmation1 = input("[+]")
        if confirmation1 == "":
            confirmation1 = "Y"
        if confirmation1 == "Y":
            remove_package(f"/home/{user}/.desktopstudio/packages/{package}")

    return