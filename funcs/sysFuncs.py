import os

def getPath():
    path = os.getcwd()
    return path

def get_folders_in_directory(directory):
    folder_names = []
    
    # Iterar sobre todos los elementos en el directorio
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        # Comprobar si es una carpeta (directorio)
        if os.path.isdir(item_path):
            folder_names.append(item)  # Añadir el nombre de la carpeta al array
    
    return folder_names