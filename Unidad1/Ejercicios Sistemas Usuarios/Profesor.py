from Usuario import Usuario

class Profesor(Usuario):
    def __init__(self, nombre, email, especialidad):
        super().__init__(nombre, email)
        self.especialidad = especialidad


    def presentacion(self):
        return f'Soy el profesor {self.get_nombre()}, especialista en {self.especialidad}'