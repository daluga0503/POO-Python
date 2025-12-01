from LibroDigital import LibroDigital
from VideoCurso import VideoCurso
from BibliotecaDigital import BibliotecaDigital
from Podcast import Podcast


libro_ejemplo = LibroDigital('Fundamentos de Ciberseguridad', 'Dra. E. Torres', 2023, 600, 'PDF')
video_ejemplo = VideoCurso('Técnicas de Ilustración Digital', 'ArtMaster', 2024, 95, 'Intermedio')
podcast_ejemplo = Podcast('El Futuro de la Energía', 'GeoTalks', 2024, 25, 'Ciencia y Medio Ambiente')
    

mi_biblioteca = BibliotecaDigital()

print('\nAÑADIENDO RECURSOS A LA BIBLIOTECA')
mi_biblioteca.anyadir_recurso(libro_ejemplo)
mi_biblioteca.anyadir_recurso(video_ejemplo)
mi_biblioteca.anyadir_recurso(podcast_ejemplo)


print('')
mi_biblioteca.listar_recursos()
mi_biblioteca.abrir_todos()


print('\nMODIFICANDO ATRIBUTOS Y COMPROBANDO ENCAPSULACIÓN')

print(f'Título anterior del VideoCurso: {video_ejemplo.get_titulo()}')
video_ejemplo.set_titulo('Técnicas de Ilustración Avanzada (Actualizado)')
print(f'Título nuevo del VideoCurso: {video_ejemplo.get_titulo()}')

print('\nIntentando modificar el año del libro a un valor inválido:')
libro_ejemplo.set_anio(-2025)

mi_biblioteca.listar_recursos()