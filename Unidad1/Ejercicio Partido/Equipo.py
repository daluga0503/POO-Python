class Equipo():
    def __init__(self, nombre, jugadores, goles = 0.0):
        if jugadores is None:
            jugadores = []
        self.nombre = nombre
        self.jugadores = jugadores
        self.goles = goles

    def add_jugadores(self, jugador):
        if len(self.jugadores) < 4:
            self.jugadores.append(jugador)
            print(f'Jugador {jugador.nombre} creado exitosamente')
        else:
            print('Error, no puedes añadir más de 5 fútbolistas al equipo')

    def add_gol(self):
        num_goles = int(input('Introduce el número de goles: '))
        goles += num_goles
    
    def __str__(self):
        print(f'Nombre del equipo: {self.nombre}, jugadores del equipo: {self.jugadores}, goles marcados: {self.goles}')