from Equipo import Equipo
class Jugador():

    def __init__(self, nombre, numero, posicion):
        self.nombre = nombre
        self.numero = numero
        self.posicion = posicion

    def add_jugadores(self, jugador):
        if len(Equipo.jugadores) < 4:
            Equipo.jugadores.append(jugador)
            print(f'Jugador {jugador.nombre} creado exitosamente')
        else:
            print('Error, no puedes añadir más de 5 fútbolistas al equipo')