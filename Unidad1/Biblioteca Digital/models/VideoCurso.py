from RecursoDigital import RecursoDigital

class VideoCurso(RecursoDigital):
    def __init__(self, titulo, autor, anio, duracion_minutos, nivel):
        super().__init__(titulo, autor, anio)
        self.duracion_minutos = duracion_minutos
        self.nivel = nivel

    def get_duracion_minutos(self):
        return self.duracion_minutos
    
    def set_duracion_minutos(self, nueva_duracion_minutos):
        if isinstance(nueva_duracion_minutos, (int, float)) and nueva_duracion_minutos > 0:
            self.duracion_minutos = nueva_duracion_minutos
        else:
            print('Error: La duración debe de ser un número entero positivo.')

    def get_nivel(self):
        return self.nivel
    
    def set_nivel(self, nueva_nivel):
        if isinstance(nueva_nivel, str) and nueva_nivel:
            self.nivel = nueva_nivel
        else:
            print('Error: El nivel debe de ser una cadena que no este vacía.')

    def abrir(self):
        return f'Iniciando la reproducción del VideoCurso {self.get_titulo()}\nNivel: {self.get_nivel()}, Duración: {self.get_duracion_minutos()} minutos.'

    def tipo(self):
        return 'Vídeo'