```
from gestonarJson import cargar, guardar, generar_id
from validacionesHerramientas import validarEntero, validar_menu, nombreValido
from historial import log
from datetime import datetime

ARCHIVO = "herramientas.json"

def agregarHerramienta():
    herramientas=cargar(ARCHIVO)

    nombre=input('Ingrese la Herramienta a agregar ')
    while nombreValido(nombre)==False or existeHerramienta(nombre)==True:
        nombre=input('Ingrese la Herramienta a agregar ')

    estadoHerramienta=validar_menu('''
                        *********************
                        seleccione una opcion:
                        1. Buen estado
                        2. Mal estado
                        *********************
                                   ''', 1, 2)
    match(estadoHerramienta):
        case 1:
            estadoHerramienta="Buen estado" 
        case 2:
            estadoHerramienta= "Mal estado"

    TipoHerramienta=validar_menu('''
                        **********************
                        seleccione una opcion:
                        1. construccion
                        2. Jardineria
                        3. Electrica 
                        **********************
                                 ''', 1, 3)
    match(TipoHerramienta):
        case 1:
            TipoHerramienta= "Construccion"
        case 2:
            TipoHerramienta= "Jardineria"
        case 3:
            TipoHerramienta= "Electrica"

    stock=validarEntero('Ingrese el stock de la herramienta ')
    while(stock==None):
        stock=validarEntero('Error, Ingrese el stock de la herramienta ')
    
    precio=float(input('Ingrese el precio de la herramienta '))
    while precio==None:
        precio=float(input('Error, Ingrese el precio del prestamo '))
    

    nueva_herramienta={
        "id": generar_id(herramientas),
        "nombre": nombre,
        "tipo": TipoHerramienta,
        "estado": estadoHerramienta,
        "precio": precio,
        "stock": stock
    }
    herramientas.append(nueva_herramienta)
    guardar(ARCHIVO, herramientas)
    print('herramienta agregada correctamente!!!!')
    log("agregarHerramienta", "se agrego una herramienta", datetime.now())

```
<img width="1611" height="996" alt="image" src="https://github.com/user-attachments/assets/200e169a-da54-46ef-b50d-383ee673364b" />
