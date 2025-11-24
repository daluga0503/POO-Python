from Publicacion import Publicacion
from Prestable import Prestable

class Libro(Publicacion, Prestable):
    def __init__(self, isbn, titulo, publication_year):
        super().__init__(isbn, titulo, publication_year)
        self.prestado = False

    def presta(self) -> None:
        if not self.prestado:
            self.prestado = True
            print(f'El libro {self.titulo} ha sido prestado')
        else:
            print(f'El libro {self.titulo} ya estaba prestado')
        
    def devuelve(self) -> None:
        if self.prestado:
            self.prestado = False
            print(f'El libro {self.titulo} ha sido devuelto')
        else:
            print(f'El libro {self.titulo} no estaba prestado')


    def estaPrestado(self) -> bool:
        return self.prestado


    def __str__(self):
        return f'Estado: {self.estado}'