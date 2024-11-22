import json

def get_value(config, section, key):
    try:
        return config[section][key]
    except KeyError:
        print(f"No se encontró la clave '{key}' en la sección '{section}'.")
        return None


def load_from_file(file_path="DesktopStudio.json"):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"El archivo {file_path} no existe.")
        return None