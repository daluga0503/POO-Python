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
        if isinstance(nuevo_titulo, str) and nuevo_titulo:
            self.__titulo = nuevo_titulo
        else:
            print('Error: EL titulo debe ser una cadena que no este vacía.')

    def set_autor(self, nuevo_autor):
        if isinstance(nuevo_autor, str) and nuevo_autor:
            self.__autor = nuevo_autor
        else:
            print('Error: El autor debe ser una cadena que no este vacía.')
    
    def set_anio(self, nuevo_anio):
        if isinstance(nuevo_anio, int) and nuevo_anio > 0:
            self.__anio = nuevo_anio
        else:
            print('Error: El año debe se un número entero positivo.')

    def descripcion_basica(self):
        return f'Titulo: {self.get_titulo()}\nAutor: {self.get_autor()}\nAño: {self.get_anio()}'
    
    @abstractmethod
    def abrir(self):
        pass

    @abstractmethod
    def tipo(self):
        pass
        
