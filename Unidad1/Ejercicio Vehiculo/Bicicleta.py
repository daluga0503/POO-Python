from Vehiculo import Vehiculo
class Bicicleta(Vehiculo):
    kmsTotalesBici = 0
    def __init__(self, kilometrosRecorridos = 0.0):
        super().__init__(kilometrosRecorridos = 0.0)
        self.kilometrosRecorridos = kilometrosRecorridos

    def andar_bici(self):
        kms = int(input('¿Cuántos kilómetros quiere recorrer?: '))
        self.kmsTotalesBici += kms
        Vehiculo.kilometrosRecorridos = kms
        
    def hacer_caballito(self):
        print('¡Estoy haciendo el caballito!')
    
    @classmethod
    def get_kms_total_bici(self):
        print(f'La bicicleta lleva recorridos {self.kmsTotalesBici} km')