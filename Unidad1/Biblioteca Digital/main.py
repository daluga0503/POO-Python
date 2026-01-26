from models.LibroDigital import LibroDigital
from models.VideoCurso import  VideoCurso
from services.BibliotecaDigital import BibliotecaDigital
from models.Podcast import Podcast
from persistence.json_manager import guardar_recursos, cargar_recursos
import traceback

RUTA_JSON = 'C:\\Users\\danie\\Documents\\Curso Especializacion\\POO-Python\\Unidad1\\Biblioteca Digital\\data\\recursos.json'

def mostrar_menu():
    print('\n=== Biblioteca de Recursos Digitales (Entrega 2 - JSON)==')
    print('1. Listar Recursos')
    print('2. Añadir Recursos')
    print('3. Guardar en JSON')
    print('4. Cargar desde JSON')
    print('5. Salir')

def menu_recursos():
    print('\n===  Recursos Digitales  ===')
    print('1. Añadir LibroDigital.')
    print('2. Añadir Podcast.')
    print('3. Añadir VideoCurso')

def form_base():
    titulo = input('Introduce el titulo: ')
    autor = input('Introduce el autor: ')
    anio = input('Introduce el año: ')
    return titulo, autor, anio

def form_libro():
    paginas = input('Introduce el número de páginas: ')
    formato = input('Introduce el formato: ')
    isbn = input('Introduce el ISBN: ')
    return paginas, formato, isbn

def form_podcast():
    num_episodio = input('Introduce el número de episodios: ')
    tema = input('Introduce el tema: ')
    duracion_min = input('Introduce la duración en Minutos: ')
    feed_url = input('Introduce la feed URL: ')
    return num_episodio, tema, duracion_min, feed_url


def form_video():
    duracion_min = input('Introduce la duración en Minutos: ')
    nivel = input('Introduce el nivel: ')
    return duracion_min, nivel

mi_biblioteca = BibliotecaDigital()


while True:
    mostrar_menu()
    try:
        opcion = int(input('Introduce la opción del menú: '))
        match opcion:
            case 1:
                mi_biblioteca.listar_recursos()
            case 2:
                menu_recursos()
                try:
                    opcion_creacion = int(input('Introduce la opción del submenú: '))
                    titulo, autor, anio = form_base()
                    match opcion_creacion:
                        case 1:
                            paginas, formato, isbn = form_libro()
                            libro = LibroDigital(titulo, autor, int(anio), int(paginas), formato, isbn)
                            mi_biblioteca.anyadir_recurso(libro)
                        case 2:
                            num_episodio, tema, duracion_min, feed_url = form_podcast()
                            podcast = Podcast(titulo, autor, int(anio), int(num_episodio), tema, int(duracion_min), feed_url)
                            mi_biblioteca.anyadir_recurso(podcast)
                        case 3:
                            duracion_min, nivel = form_video()
                            video = VideoCurso(titulo, autor, int(anio), int(duracion_min), nivel)
                            mi_biblioteca.anyadir_recurso(video)
                        case _:
                            print('Opción inválida. Introduce una opción válida.')
                    
                except ValueError as e:
                    print('Error: {e}')
            case 3:
                guardar_recursos(RUTA_JSON, mi_biblioteca.recursos)
            case 4:
                recursos = cargar_recursos(RUTA_JSON)
                for recurso in recursos:
                    print(recurso.__str__())
            case 5:
                break
            case __:
                print('Opción inválida. Introduce una opción válida.')

    except ValueError as e:
        print('Error al introducir la opción. Se espera un valor entero.')
    except Exception as e:
        print(f'Error: {e}')
        traceback.print_exc()
    





#print('')
#mi_biblioteca.listar_recursos()
#mi_biblioteca.abrir_todos()


#print('\nMODIFICANDO ATRIBUTOS Y COMPROBANDO ENCAPSULACIÓN')

#print(f'Título anterior del VideoCurso: {video_ejemplo.get_titulo()}')
#video_ejemplo.set_titulo('Técnicas de Ilustración Avanzada (Actualizado)')
#print(f'Título nuevo del VideoCurso: {video_ejemplo.get_titulo()}')

#print('\nIntentando modificar el año del libro a un valor inválido:')
#libro_ejemplo.set_anio(-2025)

#mi_biblioteca.listar_recursos()