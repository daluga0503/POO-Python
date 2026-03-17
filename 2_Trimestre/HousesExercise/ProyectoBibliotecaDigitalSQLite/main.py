from __future__ import annotations
from models import RecursoDigital, LibroDigital, VideoCurso, Podcast
from persistence.sqlite_manager import init_db, listar_recursos_db, agregar_recurso_db, borrar_recurso_db

RUTA_DB = "data/recursos.db"

#1 Muestra el menú por pantalla
def mostrar_menu() -> None:
    print("\n===Biblioteca de Recursos Digitales (Entrega 3 - SQLite)===")
    print("1. Listar Recursos")
    print("2. Añadir recursos")
    print("3. Borrar recurso")
    print("4. Salir")

#2 Listar recursos
def listar_recursos() -> None:
    recursos = listar_recursos_db(RUTA_DB)
    if not recursos:
        print("No hay recursos en la biblioteca")
        return
    
    print("--- LISTADO DE RECURSOS ---")
    for recurso in recursos:
        print(recurso)

#3 Añadir recurso
def anadir_recurso() -> None:
    recurso = crear_recurso_desde_teclado()

    if recurso is None:
        return

    id_insertado = agregar_recurso_db(RUTA_DB, recurso)
    print(f"Recurso añadido correctamente con ID {id_insertado}")

#3.1 Obtiene información del usuario para crear un nuevo recurso
def crear_recurso_desde_teclado() -> RecursoDigital:
    print("\n¿Qué tipo de recurso desea añadir?")
    print("1. Libro digital")
    print("2. Vídeo curso")
    print("3. Podcast")

    opcion = input("Elige una opción: ").strip()

    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    anio = pedir_entero("Año: ")

    match opcion:
        case "1":
            isbn = input("ISBN: ").strip()
            num_paginas = pedir_entero("Número de páginas: ")
            formato = input("Formato: ").strip()

            return LibroDigital(
                None,
                titulo,
                autor,
                anio,
                num_paginas, 
                formato, 
                isbn
            )
        
        case "2":
            duracion = pedir_entero("Duración en minutos: ")
            nivel = input("Nivel (Básico, Intermedio, Avanzado): ").strip()

            return VideoCurso(
                None,
                titulo,
                autor,
                anio,
                duracion,
                nivel
            )

        case "3":
            episodio = pedir_entero("Número de episodio: ")
            url = input("URL: ").strip()

            return Podcast(
                None,
                titulo,
                autor,
                anio,
                episodio,
                url
            )
        
        case _:
            print("Opción no válida")
            return None

#3.2 Pedir un número entero desde teclado        
def pedir_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debes introducir un número entero")

#4 Borrar un recurso
def borrar_recurso():
    id_recurso = pedir_entero("Introduce el ID del recurso a borrar: ")

    if not borrar_recurso_db(RUTA_DB, id_recurso):
        print("ERROR: No existe ningún recurso con ese ID")
    else:
        print("Recurso eliminado correctamente")

#5 Cuerpo del main
def main() -> None:
    #1 Crear esquema si no existe
    init_db(RUTA_DB)

    #3 Muestra menú
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()
        match opcion:
            case '1':
                listar_recursos()
            case '2':
                anadir_recurso()
            case '3':
                borrar_recurso()
            case '4':
                break
            case _:
                print("Opción no válida. Inténtelo de nuevo")

# Invocar al programa principal
if __name__ == "__main__":
    main()








   