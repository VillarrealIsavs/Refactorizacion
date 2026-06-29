from gestonarJson import cargar, guardar, generar_id

ARCHIVOI= "historial.json"
def log(accion, nombre, descripcion, fecha):
    lista=cargar(ARCHIVOI)
    lista.append({
        "id": generar_id(lista),
        "accion": accion,
        "nombre": nombre,
        "descripcion": descripcion,
        "fecha": fecha.isoformat()  
    })
    guardar(ARCHIVOI, lista)