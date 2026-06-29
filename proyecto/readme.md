# _Proyecto Python_

## 🎨 _Proceso:_

#### 
_Sistema de gestión integral en **Python**, estructurado mediante un modelo de Control de Inventario y Préstamos que garantiza el prestamo de las herramientas. El núcleo del código implementa una lógica de validación de stock y estados (activa, en reparación, etc...), asegurando que el inventario se actualice automáticamente tras cada transacción de préstamo o devolución. Además, un sistema de permisos basado en roles (Administrador y Usuario) para centralizar la gestión de registros y solicitudes, junto con un módulo de manejo de eventos (logs) en archivos de texto que captura errores críticos y movimientos del sistema, transformando un proceso manual propenso a pérdidas en una solución digital robusta y auditable._

                                      𓂃˖˳·˖ ִֶָ ⋆🌷͙⋆ ִֶָ˖·˳˖𓂃 ִֶָ

## 🌷_Archivos:_

#### _Se crearon 9 archivos con funciones distintas para la creacion de este proyecto llamadas:_ 
* _GestionarJson_
* _Gestionar Herramientas_
* _Gestionar Personas_
* _Gestionar Prestamos_
* _Gestionar prestamos para Administradores_
* _Historial (logs)_
* _Main_
* _Menu_
* _Validacion de herramientas_

Para mostrar un poco de lo hecho vamos a ver los siguientes 4 archivos:

### 🌹 Gestionar Json
                 ﹒⌗﹒🌹﹒౨ৎ˚₊‧
_**¿Qué hace cada función exactamente?**_

⌗ _**cargar():**  Revisa si el archivo existe; si no, devuelve una lista vacía para que el código siga corriendo sin "romperse"._

⌗ _**guardar():** Se encarga de transformar de Python al formato JSON, usando indent=4 para que el archivo sea legible para humanos si alguien lo abre en un bloc de notas._

⌗ _**generar_id():** Mira cuál fue el último número registrado y le suma 1, evitando que el usuario tenga que inventar o repetir IDs manualmente._

```
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
```



### 🪼 Gestionar Herramientas
                              ˙ . ꒷🪼 . 𖦹˙—


_Este código es el módulo de inventario, el complemento perfecto para el sistema de usuarios que vimos antes. Mientras el anterior gestionaba personas, este se encarga exclusivamente de las existencias físicas (herramientas)._

_**Registro Detallado:** Permite dar de alta herramientas categorizándolas por Tipo (Construcción, Jardinería, Eléctrica) y Estado (Buen o mal estado), además de asignarles un precio y stock inicial._
_**Control de Inventario:** Evita duplicados: La función existeHerramienta impide registrar dos veces el mismo nombre.
La función reporteStockBajo identifica automáticamente qué herramientas tienen menos de 3 unidades, facilitando la reposición.
Permite actualizar cualquier atributo de una herramienta de forma individual (usando un menú con match-case).
Permite eliminar herramientas mediante su ID._

_**Búsqueda y Visualización:** Incluye funciones para listar todo el catálogo o buscar una herramienta específica por ID, mostrando su estado y precio._

### Gestionar Personas

     ˙ . ꒷ 🍰 . 𖦹˙—

_**Persistencia de datos:** Carga y guarda información de usuarios en un archivo JSON (usuarios.json)._

_**Validación de entrada:** Utiliza funciones externas para asegurar que los nombres sean válidos y los teléfonos/IDs sean números enteros._

_**Gestión de Usuarios:** 
Genera IDs automáticos y pide datos básicos.
Permite listar todos los usuarios o buscar uno específico.
Permite modificar campos específicos (nombre, apellido, etc.) mediante un menú.
Elimina usuarios de la lista por su ID.
Registra cada acción importante con la fecha y hora exacta._

_**Flujo de Trabajo:** Incluye un sistema de "login" básico (iniciarUsuario) que da acceso a un submenú de préstamos y stock._

### 🐾 Menu 
                                                   ‧˚꒰🐾୭ ˚. ᵎᵎ
* _Centraliza todas las funciones en un solo lugar mediante menús interactivos, permitiendo que el programa no termine hasta que el usuario lo decida._
* _Administradores: Requiere una contraseña (1234). Si es correcta, otorga acceso total para gestionar el inventario, los usuarios, revisar solicitudes pendientes y ver el historial de movimientos._
* _Permite el acceso directo a la función iniciarUsuario para que los clientes puedan interactuar con el sistema de préstamos._
* _Diferencia entre un historial general (acciones exitosas) y un historial de intentos inválidos (útil para seguridad)._

_Mantiene un registro de navegación: cada vez que entras a un menú, se guarda el evento con datetime.now()._
* _Organiza el flujo de trabajo en sub-menús especializados (herramientas(), personas(), gestionadm()), lo que hace que el código sea modular y fácil de mantener._

### Contacto
_isaguvi2611@gmail.com_

### Autor
_isaguvi2611-del_
_isavs_


