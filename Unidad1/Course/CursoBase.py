from statistics import mean


class Curso:
    usuarios = {}
    calificaciones_dict =  {}
    promedio_dict ={}
    dict_cursos = {}
    
    def __init__(self, titulo, instructor, precio, clases):
        self.titulo = titulo
        self.instructor = instructor
        self.precio = precio
        self. clases = clases
        Curso.dict_cursos[self.titulo] = self

    def __str__(self):
        return f'{self.titulo}, {self.instructor}, {self.precio}, {self.clases}, {self.usuarios[self.titulo]}'
    
    def new_user_enrolled(self, name):
        if self.titulo not in Curso.usuarios:
            Curso.usuarios[self.titulo] = []
        Curso.usuarios[self.titulo].append(name)

    def received_a_rating(self, rating):
        if self.titulo not in Curso.calificaciones_dict:
            Curso.calificaciones_dict[self.titulo] = []
        Curso.calificaciones_dict[self.titulo].append(rating)
        if self.titulo not in Curso.promedio_dict:
            Curso.promedio_dict[self.titulo] = 0.0
        Curso.promedio_dict[self.titulo] = mean(Curso.calificaciones_dict[self.titulo])

    @classmethod
    def seach_course_by_name(cls, titulo):
        return cls.dict_cursos.get(titulo, 'Curso no encontrado')

    @classmethod
    def show_details(cls):
        return f'Estas son las calificaciones: {cls.calificaciones_dict}\nCalificación promedia: {cls.promedio_dict}'



