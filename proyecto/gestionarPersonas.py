
from historial import log
from datetime import datetime
from gestonarJson import cargar, guardar, generar_id
from validacionesHerramientas import validarEntero, validar_menu, nombreValido
from gestionarHerramientas import agregarHerramienta, listarHerramientas, reporteStockBajo
from gestionarPrestamos import herramientaSolicitada, prestarHerramienta, RevisarStock, prestarHerramienta, listarPrestamos, cancelarPrestamos, reportePrestamosVencidos

ARCHIVO2 = "usuarios.json"

def guardarUsuario():
    usuarios=cargar(ARCHIVO2)

    nombre=input('Ingrese el nombre del usuario a agregar ')
    while nombreValido(nombre)==False or existeUsuario(nombre)==True:
        nombre=input('Ingrese el nombre a agregar ')

    apellido=input('Ingrese el apellido del usuaro ')
    while nombreValido(apellido)==False or existeUsuario(apellido)==True:
        apellido=input('Ingrese la Herramienta a agregar ')

    direccion=input('Ingrese la direccion del usuario ')
    
    telefono=validarEntero('Ingrese su numero de telefono ')
    while(telefono==None):
        telefono=validarEntero('Error, Ingrese su numero de telefono' )


    nuevo_usuario={
        "id": generar_id(usuarios),
        "nombre": nombre,
        "apellido": apellido,
        "direccion": direccion,
        "telefono" : telefono,
    }
    usuarios.append(nuevo_usuario)
    guardar(ARCHIVO2, usuarios)
    print('usuario agregado correctamente!!!!')
    log("guardarUsuario", "se agrego un usuario", datetime.now())
    

def listarUsuarios():
    usuarios=cargar(ARCHIVO2)

    if not usuarios:
        print('No hay usuarios registrados \n')
        return
    
    for elemento in usuarios:
                
        print(f'ID: {elemento["id"]} |', end='\t')
        print(f'Nombre: {elemento["nombre"]} |' ,end='\t')
        print(f'apellido: {elemento["apellido"]} |' , end='\t')
        print(f'direccion: {elemento["direccion"]} |' , end='\t')
        print(f'telefono: {elemento["telefono"]} |' , end='\t')
        print()
    log("listarUsuarios", "se listo usuario", datetime.now())
    

def eliminarUsuario():
    contador_aux=0
    usuarios=cargar(ARCHIVO2)
    listarUsuarios()
    id_usuario=validarEntero("Escoja el id a eliminar ")
    while id_usuario==None:
        id_usuario=validarEntero("Error, Escoja el id a eliminar ")  

    for elemento in usuarios:
        if id_usuario==elemento["id"]:
            usuarios.pop(contador_aux)
            guardar(ARCHIVO2, usuarios)
            print('Usuario eliminado!!!')
        contador_aux+=1
    print('El usuario no existe\n')
    log("eliminarUsuario", "se elimino usuario", datetime.now())


def actualizarUsuario():
    usuarios=cargar(ARCHIVO2)
    listarUsuarios()
    id_usuario=validarEntero("Escoja el id a actualizar ")
    while (id_usuario==None):
        id_usuario=validarEntero("Error, Escoja el id a actualizar ")

    opActualizar=validar_menu('''
                        **********************
                        seleccione una opcion:

                        1. Nombre
                        2. Apellido
                        3. Direccion 
                        4. Telefono
                        **********************
                        ''', 1, 4)

    match opActualizar:
        case 1:
            for elemento in usuarios:
                if id_usuario==elemento["id"]:
                    nombre=input('Ingrese el nombre del usuario ')
                    while nombreValido(nombre)==False:
                        nombre=input('Ingrese el nombre del usuario ')
                    elemento["nombre"]=nombre
                    guardar(ARCHIVO2, usuarios)
                    print ('usuario actualizado correctamente!!!')
                    return
            print('No se encontro el id del usuario a actualizar \n')
        case 2:
            for elemento in usuarios:
                if id_usuario==elemento["id"]:
                    apellido=input('Ingrese el apellido del usuario ')
                    while nombreValido(apellido)==False:
                        apellido=input('Ingrese el apellido del usuario ')
                    elemento["apellido"]=apellido
                    guardar(ARCHIVO2, usuarios)
                    print ('usuario actualizado correctamente!!!')
                    return
            print('No se encontro el id del usuario a actualizar \n')
        case 3:
            for elemento in usuarios:
                if id_usuario==elemento["id"]:
                    direccion=input('Ingrese la direccion del usuario ')
                    elemento["direccion"]=direccion
                    guardar(ARCHIVO2, usuarios)
                    print ('usuario actualizado correctamente!!!')
                    return
            print('No se encontro el id del usuario a actualizar \n')
        case 4:
            for elemento in usuarios:
                if id_usuario==elemento["id"]:
                    telefono=validarEntero("Ingrese el telefono del usuario ")
                    while telefono==None:
                        telefono=validarEntero("Error, Ingrese el telefono del usuario ")
                    elemento["telefono"]=telefono
                    guardar(ARCHIVO2, usuarios)
                    print ('usuario actualizado correctamente!!!')
                    return
            print('No se encontro el id del usuario a actualizar \n')
            log("actualizarUsuario", "se actualizo usuario", datetime.now())
def buscarUsuario():
    usuarios = cargar(ARCHIVO2)
    id_usuarios = validarEntero("Ingrese el ID del usuario a buscar: ")
    if existeUsuario(id_usuarios)==False:
        print("No se encontró un usuario con ese ID ")
        return
    else:
        for usuarios in usuarios:
            if usuarios["id"] == id_usuarios:
                print(f'ID: {usuarios["id"]} | Nombre: {usuarios["nombre"]} | Apellido: {usuarios["apellido"]} | Direccion: {usuarios["direccion"]} | Telefono: {usuarios["telefono"]}')
                existeUsuario=True
                return
        print("No se encontró la herramienta con ese ID.") 
        log("buscarUsuario", "se busco un usuario", datetime.now())     
            

def existeUsuario(id_herramienta):
    listarHerramientas=cargar("herramientas.json")
    for elemento in listarHerramientas:
        if id_herramienta==elemento["id"]:
            return True
        
def iniciarUsuario():
    lista=cargar(ARCHIVO2)
    nombre=input('Ingrese su nombre para acceder ')
    for elemento in lista:
        if nombre == elemento["nombre"]:
            print('Acceso concedido,', nombre)
            prestamos()
            return
    print('Acceso no concedido,', nombre)
    log("iniciaUsuario", "se inicio usuario", datetime.now())
    

def prestamos():
    while True:
        op4=validar_menu('''
                         **********************
                        Seleccione una opcion:

                        1. Pedir herramienta
                        2. Cancelar prestamos
                        3. Dar herramienta
                        4. stock
                        5. listar prestamos
                        6. Herramientas con stock bajo
                        7. prestamos vencidos
                        8. Ver herramienta mas solicitada
                        9. salir
                        **********************
                        ''', 1, 9)
        match op4:
            case 1:
                prestarHerramienta()
            case 2:
                cancelarPrestamos()
            case 3:
                agregarHerramienta()
            case 4:
                RevisarStock()
            case 5:
                listarPrestamos()
            case 6:
                reporteStockBajo()
            case 7:
                reportePrestamosVencidos()
            case 8: 
                herramientaSolicitada()
            case 9:
                print ('....')
            case _:
                print('Opcion no valida, intente nuevamente ')
        if op4==9:
            break
        log("prestamos", "se seleccion una opcion", datetime.now())


