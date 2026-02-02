RUTA_JSON = 'C:\\Users\\dluqgal0503\\Documents\\CEPyhon\\POO\\2_Trimestre\\HousesExercise\\data\\house-price.json'
from models.House import House
from persistence.json_manager import lectura_recursos, escritura_recurso

def menu():
    print("1: Listar Nº de viviendas: ")
    print("2. Añadir vivienda")
    print("3. Salir")


def form_house():
    try:
        price = float(input('Introduce el precio de la vivienda: '))
        area = float(input('Introduce el precio de la vivienda: '))
        bedrooms = float(input('Introduce el Nº de dormitorios de la vivienda: '))
        bathrooms = float(input('Introduce el Nº de baños de la vivienda: '))
        parking = float(input('Introduce el Nº de parking de la vivienda: '))
        basement = input('Introduce si tiene sótano la vivienda (Si o No): ')
        return price, area, bedrooms, bathrooms, parking, basement 
    except ValueError as e:
        return f'Error al introducir los valores: {e}'


while True:
    menu()
    try:
        opcion = int(input('Introduce una opción del menú: '))
        match opcion:
            case 1:
                lectura_recursos(RUTA_JSON)
            case 2:
                price, area, bedrooms, bathrooms, parking, basement = form_house()
                casa = House(price, area, bedrooms, bathrooms, parking, basement)
                escritura_recurso(RUTA_JSON ,casa)
            case 3:
                break
            case _:
                print('Opción inválida. Introduce una opción válida')
    except ValueError as e:
        print(f'Error al introducir los valores: {e}')