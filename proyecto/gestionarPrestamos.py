from datetime import datetime, timedelta 
from gestonarJson import cargar, guardar, generar_id
from validacionesHerramientas import validarEntero, validar_menu, nombreValido
from gestionarHerramientas import listarHerramientas, existeHerramienta, ARCHIVO
from historial import log
from historialIntentoInvalido import log

ARCHIVO3 = "prestamos.json"

def existePersona(nombre):
    listarPrestamos=cargar(ARCHIVO3)
    for elemento in listarPrestamos:
        if nombre==elemento["nombre"]:
            return True
    

def cancelarPrestamos():
    contador_aux=0
    usuarios=cargar(ARCHIVO3)
    listarPrestamos()
    id_prestamo=validarEntero("Escoja el id a cancelar ")
    while(id_prestamo==None):
        id_prestamo=validarEntero("Error, Escoja el id  cancelar ")
        
    for elemento in usuarios:
        if id_prestamo==elemento["id"]:
            usuarios.pop(contador_aux)
            guardar(ARCHIVO3, usuarios)
            print('Se cancelo la solicitud!')
            return
        contador_aux+=1
    print("La solicitud no existe. \n")
    log("cancelarPrestamos", "se cancelo prestamo", datetime.now())
    

def solicitudesPendientes():
    listarprestamos=cargar(ARCHIVO3)
    id_prestamo=validarEntero("Ingrese el id del prestamo a revisar ")
    while id_prestamo==None:
        id_prestamo=validarEntero("Error, Ingrese el id del prestamo a revisar ")
    for elemento in listarprestamos:
         if id_prestamo==elemento["id"]:

            solicitud=validar_menu('''
                        *****************************
                        seleccione una opcion:
                                   
                        1. Aprobar
                        2. Denegar
                        3. Salir
                        *****************************
                        ''', 1, 3)
            match solicitud:
                case 1:
                    print('prestamo aprobado ')
                case 2:
                    print('prestamo no aprobado ')
                case 3:
                    print('...')
                case _:
                    print('Opcion no encontrada ')
            solicitud="Aprobado" if solicitud==1 else "Denegado"

            elemento["solicitud"]=solicitud
            guardar(ARCHIVO3, listarprestamos)
            return
         log("solicitudesPendientes", "se selecciono la opcion", datetime.now())
   

def prestarHerramienta():
    prestamos=cargar(ARCHIVO3)
    herramienta=cargar(ARCHIVO)

    nombre=input('Ingrese el nombre de la persona: ')
    while nombreValido(nombre)==False:
        nombre=input('ERROR: Ingrese el nombre de la persona valida: ')
        log("prestarHerramienta", nombre, "se ingreso un nombre erroneo ", datetime.now())

    listarHerramientas()
    herramienta_escogida=validarEntero('Ingrese la herramienta para prestar ')
    while herramienta_escogida==None:
        herramienta_escogida=validarEntero('Error, Ingrese la herramienta para prestar ')
        log("listarHerramienta", nombre, "se ingreso una herramienta erronea ", datetime.now())

    stock=validarEntero('Ingrese el stock de la herramienta a prestar ')
    while stock==None:
        stock=validarEntero('Error, Ingrese el stock de la herramienta a prestar ')
        log("stock", nombre, "no se ingreso nada", datetime.now())

    fecha_registro=datetime.today()
    dias_prestamo=int(input('ingrese los dias que desea prestar la herramienta: '))
    fecha_final_prestamo=fecha_registro+timedelta(days=dias_prestamo)
    print(fecha_final_prestamo)
    fecha_registro=datetime.today().strftime('%Y-%m-%d')
    fecha_final_prestamo=fecha_final_prestamo.strftime('%Y-%m-%d')

    for elemento in herramienta:
        if herramienta_escogida==elemento["id"]:
            precio=elemento["precio"]
            break

    preciototal=stock*precio*dias_prestamo
    for elemento in herramienta:
        if herramienta_escogida == elemento["id"]:
    
            if elemento.get("estado") == "Mal estado":
                print("error, La herramienta está en mal estado. No se puede prestar.")
                return 
            
            if stock > elemento["stock"]:
                print("error, No hay suficiente stock disponible.")
                return 
            precio = elemento["precio"]
            break

    solicitud="pendiente"
    
    nuevo_prestamo={
        "id": generar_id(prestamos) ,
        "nombre": nombre,
        "herramienta_id": herramienta_escogida,
        "solicitud": solicitud,
        "fecha_registro": fecha_registro,
        "fecha_devolucion": fecha_final_prestamo,
        "dias": dias_prestamo,
        "precio": preciototal
    }
    
    prestamos.append(nuevo_prestamo)
    guardar(ARCHIVO3,prestamos)
    print('prestamo guardado!')
    prestamos=cargar(ARCHIVO3)
    herramienta=cargar(ARCHIVO)


    for elemento2 in herramienta:
        if herramienta_escogida==elemento2["id"]:
            if stock>elemento2["stock"]:
                print('No hay suficiente stock para prestar la herramienta ')
                return
            break

    for elemento in prestamos:
        if nuevo_prestamo["id"]==elemento["id"]:
            for elemento2 in herramienta:
                if elemento["herramienta_id"]==elemento2["id"]:
                    elemento2["stock"]-=stock
                    guardar(ARCHIVO, herramienta)
                    print('Herramienta entregada!')
                    return
    print('No se encontro el prestamo')
    log("prestarHerramienta", "se presto una herramienta", datetime.now())
 

def reportePrestamosVencidos():
    prestamos=cargar(ARCHIVO3)
    today = datetime.now()
    print("Estado de Préstamos")
    
    for elemento in prestamos:
        try:
            fecha_vence=datetime.strptime(elemento['fecha_devolucion'], "%Y-%m-%d")
            estado="Vencido" if today > fecha_vence else "Activo"
        except:
            estado="Fecha no válida"
        print(f"Usuario: {elemento['nombre']} | Herramienta ID: {elemento['herramienta_id']} | Estado: {estado}")
        log("reportePrestamosVencidos", "se mostro los prestamos", datetime.now())
       
    
def listarPrestamos():
    prestamos=cargar(ARCHIVO3)

    if not prestamos:
        print('No hay prestamos registrados\n')
        return
    
    for elemento in prestamos:
                
        print(f'ID: {elemento["id"]} |', end='\t'),
        print(f'nombre: {elemento["nombre"]} |' ,end='\t'),
        print(f'Herramienta ID: {elemento["herramienta_id"]} |' , end='\t'),
        print(f'solicitud: {elemento.get("solicitud","error no existe atributo solicitud")} |' , end='\t')
        print(f'fecha registro: {elemento["fecha_registro"]} |' , end='\t'),
        print(f'fecha devolucion: {elemento["fecha_devolucion"]} |', end='\t'),
        print(f'dias: {elemento["dias"]} |', end='\t'),
        print(f'precio: {elemento.get("precio", "Atributo no disponible(precio)")} |' ,end='\t')
        print()
        log("listarPrestamos", "se listo prestamos", datetime.now())
    

def id_prestamo(lista):
    if not lista:
        return 1
    return lista [-1]["id"] + 1

def RevisarStock():
    listarHerramientas()

def herramientaSolicitada():
    prestamos=cargar(ARCHIVO3)
    herramientas=cargar(ARCHIVO)

    mayor_consulta=0
    contador=0
    nombre_herramienta=""

    for elemento in prestamos:
        for elemento2 in herramientas:
            if elemento["nombre"]==elemento2["nombre"]:
                contador+=1
        if contador>mayor_consulta:
                mayor_consulta=contador
                nombre_herramienta=elemento["nombre"]
        contador=0
    print(f'La herramienta mas solicitada es: {nombre_herramienta} con {mayor_consulta} solicitudes')
    log("herramientaSolicitada", "se solicito una herramienta", datetime.now())

def existePrestamo(id_herramienta):
    listarPrestamos=cargar("prestamos.json")
    for elemento in listarPrestamos:
        if id_prestamo==elemento["id"]:
            return True