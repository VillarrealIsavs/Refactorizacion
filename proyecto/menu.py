
from gestionarPersonas import buscarUsuario, guardarUsuario, listarUsuarios, eliminarUsuario, actualizarUsuario, iniciarUsuario
from gestionarHerramientas import agregarHerramienta, buscarHerramienta, listarHerramientas, actualizarHerramientas, eliminarHerramienta
from gestionarPrestamos import listarPrestamos, solicitudesPendientes
from gestionarPrestamosAdm import eliminarPrestamos
from validacionesHerramientas import validar_menu
from gestionarHerramientas import agregarHerramienta, buscarHerramienta, listarHerramientas, actualizarHerramientas, eliminarHerramienta
from gestionarPrestamos import listarPrestamos, solicitudesPendientes
from historial import log, ARCHIVOL
from historialIntentoInvalido import log, ARCHIVOI
from datetime import datetime
from gestonarJson import cargar,guardar, generar_id

def menu_principal():
    while True:
        op=validar_menu('''
                        *****************************
                        Bienvenido al sistema de gestion de herramientas

                        Seleccione una opcion:

                        1. Administradores
                        2. Usuarios
                        3. Salir
                        *****************************
                        ''', 1, 3)
        while op==None:
            op=validar_menu('Error, intente nuevamente: ', 1, 3)
        if op==1:
            contraseña=1234
            contraseñaReal=int(input("ingrese la contraseña: "))
            if contraseñaReal == contraseña:
                op=validar_menu('''
                                
                        *****************************
                                
                        Seleccione una opcion:
                                
                        1. herramientas
                        2. personas
                        3. gestionar prestamos
                        4. historial
                        5. salir 
                        *****************************
                        ''', 1, 5)
                match op:
                    case 1:
                        herramientas()
                    case 2:
                        personas()
                    case 3:
                        gestionadm()
                    case 4:
                        invalido=validar_menu('''
                                    selecciona una opcion
                                    1. ver historial completo
                                    2. ver historial de invalidos
                                    ''' , 1, 2)
                        match invalido:
                            case 1: 
                                historial=cargar(ARCHIVOL)
                                print(historial)
                            case 2: 
                                historialIntentoInvalido=cargar(ARCHIVOI)
                                print(historialIntentoInvalido)
                    case 5:
                        print('...')
                        break
                    case _:
                        print('No se encontro opcion ')
            else:
                print('clave incorrecta ')
        elif op==2:
            iniciarUsuario()
        elif op==3:
                print('Gracias por usar nuestro registro ')
                break
    log("menu_principal", "se mostro el menu", datetime.now())
        
def gestionadm():
    while True:
        op0=validar_menu('''
                        *****************************
                        seleccione una opcion:
                            
                        1.Solicitudes pendientes
                        2. Listar prestamos
                        3. Salir 
                        *****************************
                        ''', 1, 3)
        match op0:
            case 1:
                solicitudesPendientes()
            case 2:
                listarPrestamos()
            case 3:
                print('...')
            case _:
                print("Opcion no valida intente de nuevo ")
        if op0==3:
            break
        log("gestionadm", "se mostro las opciones", datetime.now())
    

def herramientas():
    
    while True:
        op2=validar_menu('''
                        *****************************
                        Seleccione una opcion:

                        1. Agregar herramienta
                        2. Listar herramientas
                        3. Actualizar herramientas
                        4. eliminar herramientas
                        5. Buscar herramienta
                        6. salir
                         *****************************
                        ''', 1, 6)
        match op2:
            case 1:
                agregarHerramienta()
            case 2:
                listarHerramientas()
            case 3:
                actualizarHerramientas()
            case 4:
                eliminarHerramienta()
            case 5:
                buscarHerramienta()
            case 6:
                print('...')
            case _:
                print('Opcion no valida, intente nuevamente ')
        if op2==6:
            break
        log("herramienta", "se mostro las opciones de herramienta", datetime.now())
    

def personas():
    while True:
        op3=validar_menu('''
                        *****************************
                        Seleccione una opcion:

                        1. agregar usuario
                        2. listar usuarios
                        3. actualizar usuarios
                        4. eliminar usuarios
                        5. Buscar usuario
                        6. salir
                        *****************************
                        ''', 1, 6)
        match op3:
            case 1:
                guardarUsuario()
            case 2:
                listarUsuarios()
            case 3:
                actualizarUsuario()
            case 4:
                eliminarUsuario()
            case 5:
                buscarUsuario()
            case 6:
                print('...')
            case _:
                print('Opcion no valida, intente nuevamente ')
        if op3==6:
                break
        log("personas", "se mostro las opciones", datetime.now())
