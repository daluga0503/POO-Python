from Jugador import Jugador
from Equipo import Equipo
from Partido import Partido

def menu():
    print('1. Añadir jugadores al equipo')
    print('2. Iniciar partido')
    print('3. Anotar gol')
    print('4. Mostrar resultados')
    print('5. Finalizar partido')
    print('6. Salir')

vinicius = Jugador('Vinicius Jr', 7, 'Delantero')
mbappe = Jugador('Kylian Mbappé', 10, 'Delantero')
belligham = Jugador('Jude Bellingham', 5, 'Centrocampista')
jugadores_realMadrid = [vinicius, mbappe, belligham]

lamine = Jugador('Lamine Yamal', 10, 'Delantero')
rapinha = Jugador('Raphinha', 11, 'Delantero')
pedri = Jugador('Pedri', 8, 'Centrocampista')
cubarsi = Jugador('Pau Cubarsi', 4, 'Defensa')
terStegen = Jugador('Marc-André ter Stegen', 1, 'Portero')
jugadores_barcelona = [lamine, rapinha, pedri]

realMadrid = Equipo('Real Madrid', jugadores_realMadrid)
barcelona = Equipo('FC Barcelona', jugadores_barcelona)

partido = Partido(realMadrid, barcelona)

while True: 
    menu()
    opcion = int(input('Selecciona una opción: '))

    match opcion:
        case 1:
            equipo_seleccionado = int(input('¿A qué equipo quieres añadir jugadores? (1: Real Madrid, 2: FC Barcelona): '))
            nombre = input('Introduce el nombre del jugador: ')
            numero = int(input('Introduce el número del jugador: '))
            posicion = input('Introduce la posición del jugador: ')
            nuevo_jugador = Jugador(nombre, numero, posicion)

            if equipo_seleccionado == 1:
                realMadrid.add_jugadores(nuevo_jugador)
            elif equipo_seleccionado == 2:
                barcelona.add_jugadores(nuevo_jugador)
            else:
                print('Equipo no válido.')

        case 2:
            partido.comenzar_partido()
        case 3:
            equipo_gol = int(input('¿Qué equipo anota el gol? (1: Real Madrid, 2: FC Barcelona): '))
            if equipo_gol == 1:
                jugador_nombre = input('Introduce el nombre del jugador que anota el gol: ')
                jugador = next((j for j in jugadores_realMadrid if j.nombre == jugador_nombre), None)
                if jugador:
                    partido.anotar_gol(1, jugador)
                else:
                    print('Jugador no encontrado en Real Madrid.')
            elif equipo_gol == 2:
                jugador_nombre = input('Introduce el nombre del jugador que anota el gol: ')
                jugador = next((j for j in jugadores_barcelona if j.nombre == jugador_nombre), None)
                if jugador:
                    partido.anotar_gol(2, jugador)
                else:
                    print('Jugador no encontrado en FC Barcelona.')
            else:
                print('Equipo no válido.')
        case 4:
            partido.mostar_resultados()
        case 5:
            partido.finalizar_partido()
        case 6:
            print('Saliendo del programa.')
            break
        case _:
            print('Opción no válida. Por favor, intenta de nuevo.')



