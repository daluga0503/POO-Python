from statistics import mean
import PdfCourse as PdfCourse
import VideoCourse as VideoCourse


class Curso:
    usuarios = []
    calificaciones = []
    promedio = 0.0
    
    def __init__(self, titulo, instructor, precio, clases):
        self.titulo = titulo
        self.instructor = instructor
        self.precio = precio 
        self. clases = clases

    def __str__(self):
        return f'{self.titulo}, {self.instructor}, {self.precio}, {self.clases}, {self.usuarios}'
    
    def new_user_enrolled(self, name):
        Curso.usuarios.append(name)

    def received_a_rating(self, rating):
        self.calificaciones.append(rating)
        self.promedio = mean(self.calificaciones)

    def show_details(self):
        return f'Estas son las calificaciones: {self.calificaciones}\nCalificación promedia: {self.promedio}'


curso1 = VideoCourse('Curso1', 'Pepe', 25, 5, 150)
