class Vehiculo():
    vehiculosCreados = []
    kilometrosTotales = 0

    def __init__(self, kilometrosRecorridos = 0.0):
        self.kilometrosRecorridos = kilometrosRecorridos
        Vehiculo.kilometrosTotales += kilometrosRecorridos
        Vehiculo.vehiculosCreados.append(self)

    @classmethod
    def get_kms_totales(Vehiculo):
        print(f'Los vehículos llevan recorridos {Vehiculo.kilometrosTotales} km')