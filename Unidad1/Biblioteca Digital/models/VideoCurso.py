from models.RecursoDigital import RecursoDigital
from typing import Dict, Any

class VideoCurso(RecursoDigital):
    def __init__(self, titulo, autor, anio, duracion_minutos, nivel):
        super().__init__(titulo, autor, anio)
        self.__duracion_minutos = duracion_minutos
        self.__nivel = nivel
        self.__tipo = 'VideoCurso'

    @property
    def duracion_minutos(self):
        return self.__duracion_minutos
    
    @duracion_minutos.setter
    def duracion_minutos(self, nueva_duracion_minutos):
        if isinstance(nueva_duracion_minutos, (int, float)) and nueva_duracion_minutos > 0:
            self.__duracion_minutos = nueva_duracion_minutos
        else:
            print('Error: La duración debe de ser un número entero positivo.')

    @property
    def nivel(self):
        return self.__nivel
    
    @nivel.setter
    def nivel(self, nueva_nivel):
        if isinstance(nueva_nivel, str) and nueva_nivel:
            self.__nivel = nueva_nivel
        else:
            print('Error: El nivel debe de ser una cadena que no este vacía.')

    def abrir(self):
        return f'Iniciando la reproducción del VideoCurso {self.__titulo}\nNivel: {self.__nivel}, Duración: {self.__duracion_minutos} minutos.'

    def tipo(self):
        return 'Vídeo'
    
    def to_dict(self) -> Dict[str, Any]:
        diccionario_video = super().to_dict()
        diccionario_video.update({
            "duracion_minutos": self.__duracion_minutos,
            "nivel": self.__nivel,
            "tipo": self.__tipo
        })
        return diccionario_video
    
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "VideoCurso":
        return VideoCurso(
            data["recurso_id"], data["titulo"], data["autor"], data["anio"], data["duracion_minutos"], data["nivel"]
        )