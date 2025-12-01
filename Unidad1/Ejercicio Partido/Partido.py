class Partido():
    def __init__(self, rival1, rival2, goles_rival1 = 0, goles_rival2 = 0):
        self.rival1 = rival1
        self.rival2 = rival2
        self.goles_rival1 = goles_rival1
        self.goles_rival2 = goles_rival2

    def anotar_gol(self, rival, jugador):
        if rival == 1:
            self.goles_rival1 += 1
        else:
            self.goles_rival2 += 1
        print(f'Gooooooooooool de {jugador.nombre}')

    def mostar_resultados(self):
        print(f'El resultado es {self.rival1.nombre} {self.goles_rival1} - {self.goles_rival2} {self.rival2.nombre}')

    def comenzar_partido(self):
        print(f'Piiii. Comienza el partido entre el {self.rival1.nombre} y el {self.rival2.nombre}')

    def finalizar_partido(self):
        print(f'Pi Pi Piiii. final del partido entre el {self.rival1.nombre} y el {self.rival2.nombre}')

    