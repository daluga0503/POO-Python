from Usuario import Usuario

class Alumno(Usuario):
    def __init__(self, nombre, email, curso, nota_media):
        super().__init__(nombre, email)
        self.curso = curso
        self.nota_media = nota_media

    def presentacion(self):
        return f'Soy {self.get_nombre()}, estudiante de {self.curso}, con una nota media de: {self.nota_media}'
    

