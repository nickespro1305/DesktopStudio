import subprocess
import os
import getpass

def rn(plugin):
    user = getpass.getuser()
    os.chdir(f"/home/{user}/.desktopstudio/plugins/{plugin}")
    subprocess.run(f"./{plugin}", shell=True, check=True)
    return