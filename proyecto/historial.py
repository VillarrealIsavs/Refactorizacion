from gestonarJson import cargar, guardar, generar_id
ARCHIVOL= "historial.json"
def log(accion, descripcion, fecha):
    
    lista=cargar(ARCHIVOL)
    lista.append({
        "id": generar_id(lista),
        "accion": accion,
        "descripcion": descripcion,
        "fecha": fecha.isoformat()  
    })
    guardar(ARCHIVOL, lista)