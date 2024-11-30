from funcs.sysFuncs import *
from rich.console import Console
import getpass

def confirmation(header, icon, autoy):
    console = Console()

    # imprimimos el header y el icono
    console.print(header)
    confirmation = console.input(icon)

    # algunos ajustes
    if confirmation == "" and autoy == 1:
            confirmation = "Y"
    return confirmation

def askForFlavour(icon):
      console = Console()
      user = getpass.getuser()
      avariableFlavours = get_folders_in_directory(f"/home/{user}/.desktopstudio/packages")
      console.print(avariableFlavours)
      flavour = console.input(icon)
      return flavour

def askForPlugin():
      return

def askForName(icon, autoy):
      console = Console()
      console.print("this project needs a [red]name[/red], write here one")
      name = console.input(icon)
      if name == "" and autoy == 1:
            name = "test1"
            console.print(f"oops, you forgotten to specify a [red]name[/red] for the project, dont worry, we created it for you :D, say hello to [red]{name}[/red]!")
      else:
            console.print(f"{name}, thats a beautifull name")
      return name