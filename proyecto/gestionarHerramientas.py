
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

def listarHerramientas():
    herramientas=cargar(ARCHIVO)

    if not herramientas:
        print('No hay herramientas registradas\n')
        return

    for elemento in herramientas:
                
        print(f'ID: {elemento["id"]} |', end='\t')
        print(f'Nombre: {elemento["nombre"]} |' ,end='\t')
        print(f'Tipo: {elemento["tipo"]} |' , end='\t')
        print(f'Estado: {elemento["estado"]} |' ,end='\t')
        print(f'precio: {elemento.get("precio", "Atributo no disponible(precio)")} |' ,end='\t')
        print(f'Stock: {elemento.get("stock", "Atributo no disponible(stock)")} |' ,end='\t')
        print()
    log("listarHerramienta", "se listo las herramienta", datetime.now())

def reporteStockBajo():
    limite=3
    herramienta=cargar(ARCHIVO)
    print('Herramientas con stock bajo: ')
    for elemento in herramienta:
        if elemento["stock"]<limite:
            print(f'ID: {elemento["id"]}', end='\t'),
            print(f'nombre: {elemento["nombre"]}' ,end='\t'),
            print(f'stock: {elemento["stock"]}' , end='\t')
            print()
            return
    print('No hay herramientas con stock bajo')
    log("reportesStockBajo", "se listo el stock bajo", datetime.now())
    

def actualizarHerramientas():
    herramientas=cargar(ARCHIVO)
    listarHerramientas()
    id_herramienta=validarEntero("Escoja el id a actualizar ")
    while (id_herramienta==None):
        id_herramienta=validarEntero("Error, Escoja el id a actualizar ")

    opActualizar=validar_menu('''
                        **********************
                        seleccione una opcion:
                              
                        1. Nombre
                        2. Tipo
                        3. estado 
                        4. precio
                        5. stock
                     **********************
                        ''', 1, 5)

    match opActualizar:
        case 1:
            for elemento in herramientas:
                if id_herramienta==elemento["id"]:
                    nombre=input('Ingrese el nombre de la herramienta ')
                    while nombreValido(nombre)==False:
                        nombre=input('Ingrese el nombre de la herramienta ')
                    elemento["nombre"]=nombre
                    guardar(ARCHIVO, herramientas)
                    print ('herramienta actualizada correctamente!!!')
                    return
            print('No se encontro el id de la herramienta a actualizar \n')
        case 2:
            for elemento in herramientas:
                if id_herramienta==elemento["id"]:
                    tipoHerramienta=input('Ingrese el tipo de la herramienta ')
                    while nombreValido(tipoHerramienta)==False:
                        tipoHerramienta=input('Ingrese el tipo de la herramienta  ')
                    elemento["tipo"]=tipoHerramienta
                    guardar(ARCHIVO, herramientas)
                    print ('herramienta actualizada correctamente!!!')
                    return
            print('No se encontro el id de la herramienta a actualizar \n')
        case 3:
            for elemento in herramientas:
                if id_herramienta==elemento["id"]:
                    estadoHerramienta=validar_menu('''
                        **********************
                        seleccione una opcion:
                                                   
                        1. Buen estado
                        2. Mal estado
                        **********************
                                   ''', 1, 2)
                    
                    while estadoHerramienta == None:
                        estadoHerramienta=validar_menu('Error opcion no encontrada')
                    estadoHerramienta= "Buen estado" if estadoHerramienta == 1 else "Mal estado"
                    elemento["estado"]=estadoHerramienta
                    guardar(ARCHIVO, herramientas)
                    print ('herramienta actualizada correctamente!!!')
                    return
            print('No se encontro el id de la herramienta a actualizar \n')

        case 4:
            for elemento in herramientas:
                if id_herramienta==elemento["id"]:
                    precio=input('Ingrese el precio de la herramienta ')
                    while nombreValido(precio)==False:
                        precio=input('Ingrese el precio de la herramienta ')
                    elemento["precio"]=precio
                    guardar(ARCHIVO, herramientas)
                    print ('herramienta actualizada correctamente!!!')
                    return
            print('No se encontro el id de la herramienta a actualizar \n')

        case 5:
            for elemento in herramientas:
                if id_herramienta==elemento["id"]:
                    stock=validarEntero("Ingrese el stock de la herramienta ")
                    while stock==None:
                        stock=validarEntero("Error, Ingrese el stock de la herramienta ")
                    elemento["stock"]=stock
                    guardar(ARCHIVO, herramientas)
                    print ('herramienta actualizada correctamente!!!')
                    return
            print('No se encontro el id de la herramienta a actualizar \n')
    log("actualizarHerramienta", "se actualiza una herramienta", datetime.now())

def eliminarHerramienta():
    contador=0
    herramientas=cargar(ARCHIVO)
    listarHerramientas()
    id_herramienta=validarEntero("Escoja el id a eliminar ")
    while (id_herramienta==None):
        id_herramienta=validarEntero("Error, Escoja el id a eliminar ")
    for elemento in herramientas:
        if id_herramienta==elemento["id"]:
            herramientas.pop(contador)
            guardar(ARCHIVO, herramientas)
            print('herramienta eliminada correctamente!!!')
            return
        contador+=1
    print('No se encontro el id de la herramienta a eliminar \n')
    log("eliminarHerramienta", "se elimino una herramienta", datetime.now())

def existeHerramienta(nombre):
    herramientas=cargar(ARCHIVO)
    for elemento in herramientas:
        if nombre.lower()==elemento["nombre"].lower():
            print('El nombre de la herramienta ya existe')
            return True
    return False

def buscarHerramienta():
        herramientas = cargar(ARCHIVO)
        id_herramienta = validarEntero("Ingrese el ID de la herramienta a buscar: ")
        if id_herramienta==None:
            print("No se encontró una herramienta ")
            return
        else:
            for herramienta in herramientas:
                if herramienta["id"] == id_herramienta:
                    print(f'ID: {herramienta["id"]} -> Nombre: {herramienta["nombre"]} -> Tipo de herramienta: {herramienta["tipo"]} -> Estado: {herramienta["estado"]} -> Stock: {herramienta["stock"]} ')
                    id_herramienta=True
                    return
            print("No se encontró la herramienta con ese ID.")
        log("buscarHerramienta", "se busco una herramienta", datetime.now())
        
