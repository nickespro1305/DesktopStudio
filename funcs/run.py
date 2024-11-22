from funcs.jsonFuncs import load_from_file, get_value
import subprocess

def run(script):
    # Acceso a valores
    loaded_config = load_from_file()
    dev_script = get_value(loaded_config, "scripts", "dev")
    if script == "dev":
        subprocess.run(dev_script, shell=True, check=True)
    return