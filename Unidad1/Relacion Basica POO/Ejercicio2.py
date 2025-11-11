"""
Haz una lista con los atributos que podría tener la clase caballo. 
A continuación haz una lista con los posibles métodos (acciones asociadas a los caballos). 
Hecho esto implementa la clase Caballo y pruébala creando instancias y aplicándole algunos métodos.

Métodos:
saludar, comer, andar, relinchar, correr

Ejemplo:
Hola, me llamo Babieca
Tocotoc tocotoc tocotoc
Hiiiiiiieeeeee
Hola, yo soy Lykos
Ñam ñam ñam
Tocotoc tocotoc tocotoc
"""

class Caballo():
    def __init__(self, nombre, edad, color, raza, establo ):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.raza = raza
        self.establo = establo

    def saludar(self):
        print(f'Hola, me llamo {self.nombre}')

    def comer(self):
        print('Ñam ñam ñam')

    def correr (self):
        print('Tocotoc tocotoc tocotoc')

    def relinchar(self):
        print('Hiiiiiiieeeeee')

if __name__ == '__main__':
    caballo1 = Caballo('Babieca', 2, 'Marrón', 'Frisón', 'Palacio Versalles')
    caballo2 = Caballo('Lykos', 5, 'Blanco', 'Árabe', 'Palacio Versalles')

    caballo1.saludar()
    caballo1.correr()
    caballo1.relinchar()
    caballo2.saludar()
    caballo2.comer()
    caballo2.correr()
