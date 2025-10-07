class Book():
    def __init__(self, isbn, titulo, autor, editorial, paginas, precio, ejemplares):
        self.isbn = isbn
        self. titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.paginas = paginas
        if precio < 50 and precio > 1000:
            self.precio = precio
        self.ejemplares = ejemplares

    def display(self):
        print(f'ISBN: {self.isbn}\nTitulo: {self.titulo}\nPrecio: {self.precio}\nNº Copias: {self.ejemplares}')

    def in_stock(self):
        if self.ejemplares >0:
            return True
        else:
            return False
        


book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

books = [book1, book2, book3, book4]

for book in books:
    book.display()
    print()

print(f'\nLibros de Jack\n')
jack_books = [book for book in books if book.autor == 'Jack']
for book in jack_books:
    print(f'Titulo: {book.titulo}')
