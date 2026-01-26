from abc import ABC, abstractmethod
from typing import Dict, Any
class RecursoDigital(ABC):
    def __init__(self, titulo, autor, anio):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, str) and nuevo_titulo:
            self.__titulo = nuevo_titulo
        else:
            print('Error: EL titulo debe ser una cadena que no este vacía.')

    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, nuevo_autor):
        if isinstance(nuevo_autor, str) and nuevo_autor:
            self.__autor = nuevo_autor
        else:
            print('Error: El autor debe ser una cadena que no este vacía.')
    
    @property
    def anio(self):
        return self.__anio
    
    @anio.setter
    def anio(self, nuevo_anio):
        if isinstance(nuevo_anio, int) and nuevo_anio > 0:
            self.__anio = nuevo_anio
        else:
            print('Error: El año debe se un número entero positivo.')

    def descripcion_basica(self):
        return f'Titulo: {self.__titulo}\nAutor: {self.__autor}\nAño: {self.__anio}'
    
    @abstractmethod
    def abrir(self):
        pass

    @abstractmethod
    def tipo(self):
        pass


    def to_dict(self) -> Dict[str, Any]:
        return {
            "tipo": self.tipo,
            "titulo": self.__titulo,
            "autor": self.__autor,
            "anio": self.__anio
        }
    @staticmethod  
    def from_dict(data: Dict[str,Any]) -> "RecursoDigital":
        from models.LibroDigital import LibroDigital
        from models.Podcast import Podcast
        from models.VideoCurso import VideoCurso

        match data["tipo"]:
            case "LibroDigital": return LibroDigital.from_dict(data)
            case "Podcast": return Podcast.from_dict(data)
            case "VideoCurso": return VideoCurso.from_dict(data)
            case _: raise  ValueError("Tipo Inválido")
