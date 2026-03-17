# RUTA_JSON = 'C:\\Users\\dluqgal0503\\Documents\\CEPyhon\\POO\\2_Trimestre\\HousesExercise\\data\\house-price.json'
RUTA_JSON = 'C:\\Users\\danie\\Documents\\Curso Especializacion\\POO-Python\\2_Trimestre\\HousesExercise\\data\\house-price.json'
from models.House import House
from persistence.json_manager import lectura_recursos, escritura_recurso

def menu():
    print("1: Listar Nº de viviendas: ")
    print("2. Añadir vivienda")
    print("3. Salir")


def form_house():
    try:
        price = float(input('Introduce el precio de la vivienda: '))
        area = float(input('Introduce el área de la vivienda: '))
        bedrooms = float(input('Introduce el Nº de dormitorios de la vivienda: '))
        bathrooms = float(input('Introduce el Nº de baños de la vivienda: '))
        parking = int(input('Introduce el Nº de parking de la vivienda: '))
        basement = input('Introduce si tiene sótano la vivienda (Si o No): ').lower()

        basement = 'yes' if basement == 'si' else 'no'
        return price, area, bedrooms, bathrooms, parking, basement
    except ValueError as e:
        print(f'Error al introducir los valores: {e}')
        return None


while True:
    menu()
    try:
        opcion = int(input('Introduce una opción del menú: '))
        match opcion:
            case 1:
                try:
                    num_registro = int(input('Introduce cuantos registros quieres listar: '))
                    viviendas = lectura_recursos(RUTA_JSON, num_registro)
                    print(f"\n--- Listado de {len(viviendas)} viviendas ---")
                    for i, v in enumerate(viviendas, 1):
                        # Aquí usas los @property que creaste: v.price, v.area, etc.
                        print(f"{i}. Precio: {v.price}€ - Área: {v.area}m² - Sótano: {'Sí' if v.basement =='yes' else 'No'}")
                except ValueError as e:
                    print('Error, introduce u valor correcto: {e}')
            case 2:
                price, area, bedrooms, bathrooms, parking, basement = form_house()
                casa = House(price, area, bedrooms, bathrooms, parking, basement)
                anadido = escritura_recurso(RUTA_JSON ,casa)
                if anadido == True:
                    print('Vivienda añadida exitosamente')
                else:
                    print('No se pudo añadir la vivienda')
            case 3:
                break
            case _:
                print('Opción inválida. Introduce una opción válida')
    except ValueError as e:
        print(f'Error al introducir los valores: {e}')