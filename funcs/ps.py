from funcs.sysFuncs import get_folders_in_directory
from rich.console import Console
from rich.table import Table
import getpass

def ps():
    user = getpass.getuser()
    console = Console()
    flavours = get_folders_in_directory(f"/home/{user}/.desktopstudio/packages")

    console.print(flavours)