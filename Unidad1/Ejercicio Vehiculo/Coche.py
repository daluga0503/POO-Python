from Vehiculo import Vehiculo
class Coche(Vehiculo):
    kmsTotalesCoche = 0
    def __init__(self, kilometrosRecorridos=0.0):
        super().__init__(kilometrosRecorridos = 0.0)
        self.kilometrosRecorridos = kilometrosRecorridos

    def andar_coche(self):
        kms = int(input('¿Cuántos kilómetros quiere recorrer?: '))
        self.kmsTotalesCoche += kms
        self.kilometrosRecorridos += kms
        Vehiculo.kilometrosTotales += kms

    def quemar_rueda(self):
        print('!Estoy quemando rueda con el coche!')
    
    def get_kms_total_coche(self):
        print(f'El coche lleva recorridos {self.kmsTotalesCoche} km')