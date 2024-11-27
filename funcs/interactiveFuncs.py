from rich.console import Console

def confirmation(header, icon, autoy):
    console = Console()

    # imprimimos el header y el icono
    console.print(header)
    confirmation = console.input(icon)

    # algunos ajustes
    if confirmation == "" and autoy == 1:
            confirmation = "Y"
    return confirmation