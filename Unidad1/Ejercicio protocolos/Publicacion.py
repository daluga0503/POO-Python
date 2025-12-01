class Publicacion():
    def __init__(self, isbn, titulo, publication_year):
        self.isbn = isbn
        self.titulo = titulo
        self.publication_year = publication_year

    def __str__(self):
        return f'Titulo: {self.titulo}, Año de publicación: {self.publication_year}, ISBN: {self.isbn}'
    