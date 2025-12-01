from Publicacion import Publicacion
class Revista(Publicacion):
    def __init__(self, isbn, titulo, publication_year, numero):
        super().__init__(isbn, titulo, publication_year)
        self.numero = numero

    def __str__(self):
        return f'Revista: {self.titulo}, Nº: {self.numero}, Año Publicación: {self.publication_year} - ISBN: {self.isbn}'