
def validarEntero(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        return None
    
def validar_menu(mensaje, minimo, maximo):
    try:
        dato=int(input(mensaje))
        if dato<minimo or dato>maximo:
            return None
        else:
            return dato
    except:
        return None
    
def nombreValido(nombre):
    if nombre.strip()=="":
        print('nombre vacio')
        return nombre
    return nombre

