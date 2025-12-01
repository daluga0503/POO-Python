"""
Crea la clase Vehiculo, así como las clases Bicicleta y Coche como subclases de la primera. 
Para la clase Vehiculo, crea los atributos de clase vehiculosCreados y kilometrosTotales, así como el atributo de instancia kilometrosRecorridos. 
Crea también algún método específico para cada una de las subclases. Prueba las clases creadas mediante un programa con un menú como el que se muestra en el ejemplo:

1. Anda con la bicicleta
2. Haz el caballito con la bicicleta
3. Anda con el coche
4. Quema rueda con el coche
5. Ver kilometraje de la bicicleta
6. Ver kilometraje del coche
7. Ver kilometraje total
8. Salir
Elige una opción (1-8):

"""

class Vehiculo():
    vehiculosCreados = []
    kilometrosTotales = 0

    def __init__(self, kilometrosRecorridos = 0.0):
        self.kilometrosRecorridos = kilometrosRecorridos
        Vehiculo.vehiculosCreados.append(self)
        Vehiculo.kilometrosTotales += kilometrosRecorridos

    @classmethod
    def get_kms_totales(cls):
        print(f'Los vehículos han recorrido {cls.kilometrosTotales} kms totales')


class Bicicleta(Vehiculo):
    kilometrosTotalesBici = 0
    def __init__(self, kilometrosRecorridos = 0.0):
        super().__init__(kilometrosRecorridos = 0.0)
        self.kilometrosRecorridos = kilometrosRecorridos

    def andar_bici(self):
        kms = int(input('¿Cuántos kilómetros quiere recorrer?: '))
        Bicicleta.kilometrosTotalesBici += kms
        self.kilometrosRecorridos += kms
        Vehiculo.kilometrosTotales += kms
        
    def hacer_caballito(self):
        print('¡Estoy haciendo el caballito!')
    
    @classmethod
    def get_kms_total_bici(cls):
        print(f'La bicicleta lleva recorridos {cls.kilometrosTotalesBici} km')


class Coche(Vehiculo):
    kilometrosTotalesCoche = 0

    def __init__(self, kilometrosRecorridos=0.0):
        super().__init__(kilometrosRecorridos = 0.0)
        self.kilometrosRecorridos = kilometrosRecorridos

    def andar_coche(self):
        kms = int(input('¿Cuántos kilómetros quiere recorrer?: '))
        Coche.kilometrosTotalesCoche += kms
        self.kilometrosRecorridos += kms
        Vehiculo.kilometrosTotales += kms

    def quemar_rueda(self):
        print('!Estoy quemando rueda con el coche!')
    
    @classmethod
    def get_kms_total_coche(cls):
        print(f'El coche lleva recorridos {cls.kilometrosTotalesCoche} km')

if __name__ == '__main__':
    
    salir = False
    def menu():
        print('1. Anda con la bicicleta')
        print('2. Haz el caballito con la bicicleta')
        print('3. Anda con el coche')
        print('4. Quema rueda con el coche')
        print('5. Ver kilometraje de la bicicleta')
        print('6. Ver kilometraje del coche')
        print('7. Ver kilometraje total')
        print('8. Salir')

    bici = Bicicleta()
    coche = Coche()
    while salir==False:
        menu()
        opcion = int(input('Elige una opción (1-8): '))


        match opcion:
            case 1:
                bici.andar_bici()
            case 2:
                bici.hacer_caballito()
            case 3:
                coche.andar_coche()
            case 4:
                coche.quemar_rueda()
            case 5:
                bici.get_kms_total_bici()
            case 6:
                coche.get_kms_total_coche()
            case 7:
                Vehiculo.get_kms_totales()
            case 8:
                salir = True
            case _:
                print('Introduce una opción correcta')