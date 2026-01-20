from models.LibroDigital import LibroDigital
from models.VideoCurso import  VideoCurso
from models.BibliotecaDigital import BibliotecaDigital
from models.Podcast import Podcast
from persistence.json_manager import json_manager

RUTA_JSON = 'data/recursos.json'

def mostrar_menu():
    print('\n=== Biblioteca de Recursos Digitales (Entrega 2 - JSON)==')
    print('1. Listar Recursos')
    print('2. Añadir Recursos')
    print('3. Guardar    en JSON')
    print('4. Cargar desde JSON (reemplaza la lista actual)')
    print('5. Salir')

def alta_recurso():
    pass



while True:
    mostrar_menu()
    try:
        opcion = int(input('Introduce la opción del menú: '))
        match opcion:
            case 1:
                BibliotecaDigital.listar_recursos
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                break
            case __:
                print('Opción inválida. Introduce una opción válida.')

    except Exception as e:
        print('Error al introducir la opción. Se espera un valor entero.')




# libro_ejemplo = LibroDigital('Fundamentos de Ciberseguridad', 'Dra. E. Torres', 2023, 600, 'PDF')
#video_ejemplo = VideoCurso('Técnicas de Ilustración Digital', 'ArtMaster', 2024, 95, 'Intermedio')
#podcast_ejemplo = Podcast('El Futuro de la Energía', 'GeoTalks', 2024, 25, 'Ciencia y Medio Ambiente')
    

#mi_biblioteca = BibliotecaDigital()

#print('\nAÑADIENDO RECURSOS A LA BIBLIOTECA')
#mi_biblioteca.anyadir_recurso(libro_ejemplo)
#mi_biblioteca.anyadir_recurso(video_ejemplo)
#mi_biblioteca.anyadir_recurso(podcast_ejemplo)


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