import os
import json

def cargar(herramientas):
    if not os.path.exists(herramientas): 
        return []
    try:
        with open(herramientas, "r") as archivo: 
            return json.load(archivo)
    except json.JSONDecodeError: 
        return []
    
def guardar(herramientas, datos):
    with open (herramientas, "w") as archivo:
        json.dump(datos, archivo, indent=4)

def generar_id(lista):
    if not lista:
        return 1
    return lista [-1]["id"] + 1