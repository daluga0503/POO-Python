from abc import ABC, abstractmethod

class RecursoDigital(ABC):
    def __init__(self, titulo, autor, anio):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor
    
    def get_anio(self):
        return self.__anio
    
    def set_titulo(self, nuevo_titulo):
       self.__titulo = nuevo_titulo

    def set_autor(self, nuevo_autor):
        self.__autor = nuevo_autor
    
    def set_anio(self, nuevo_anio):
        self.__anio = nuevo_anio

    @abstractmethod
    def descripcion_basica(self):
        pass
        
