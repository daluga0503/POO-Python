from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, email):
        self.__nombre = nombre
        self.__email = email

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email
    
    def set_nombre(self, nuevo_nombre):
        if self.__nombre != nuevo_nombre:
            self.__nombre = nuevo_nombre
        else:
            print('El nuevo atributo es igual que el anterior')
            

    
    def set_email(self, nuevo_email):
        if self.__email != nuevo_email:
            self.__email = nuevo_email
        else:
            print('El nuevo atributo es igual que el anterior')
    
    @abstractmethod
    def presentacion(self):
        pass