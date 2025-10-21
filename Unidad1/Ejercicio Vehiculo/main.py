from Coche import Coche
from Bicicleta import Bicicleta
from Vehiculo import Vehiculo

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