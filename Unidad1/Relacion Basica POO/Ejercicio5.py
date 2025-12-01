"""
Crea la clase Fraccion. Los atributos serán numerador y denominador. Y algunos de los métodos pueden ser invierte, simplifica, multiplica, divide, etc. 
Prueba la clase creada en un programa en el que se instancien objetos y se les apliquen métodos.
Ejemplo:
-7/8 x 5 = -35/8
-7/8 ^-1 = -8/7
-7/8 x 3/5 = -21/40
-7/8 : 3/5 = -35/24
-910/350 = -13/5
"""
import math

class Fraccion():
    def __init__(self, numerador, denominador=1):
        if denominador == 0:
            raise ZeroDivisionError('El denominador no puede ser 0')
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f'{self.numerador} / {self.denominador}'


    def invierte(self):
        if self.denominador == 0:
            return ZeroDivisionError('No se puede invertir una fracción con numerador 0')
        return Fraccion(self.denominador, self.numerador)
    
    def simplifica(self):
        mcd = math.gcd(self.numerador, self.denominador)
        return Fraccion (self.numerador // mcd, self.denominador // mcd)
        

    def multiplica(self, otro):
        if isinstance(otro, Fraccion):
            return Fraccion(self.numerador * otro.numerador, self.denominador * otro.denominador).simplifica()
        elif isinstance(otro, int):
            return Fraccion(self.numerador * otro, self.denominador).simplifica()
        else:
            raise TypeError('Se puede multiplicar solo por Fracción o un número entero.')

    def divide(self, otro):
        if isinstance(otro, Fraccion):
            return Fraccion(self.numerador * otro.denominador, self.denominador * otro.numerador).simplifica()
        elif isinstance(otro, int):
            return Fraccion(self.numerador, self.denominador * otro).simplifica()
        else:
            raise TypeError('Se puede dividir solo pro una Fracción o un entero.')


if __name__ == '__main__':
    # Instanciamos fracciones
    f1 = Fraccion(-7, 8)
    f2 = Fraccion(3, 5)

    print("Fracción inicial:", f1)                # -7/8
    print("Multiplicación por entero:", f1.multiplica(5))   # -35/8
    print("Inversa:", f1.invierte())              # -8/7
    print("Multiplicación por fracción:", f1.multiplica(f2)) # -21/40
    print("División por fracción:", f1.divide(f2))           # -35/24

    # Simplificación
    f3 = Fraccion(-910, 350)
    print("Fracción simplificada:", f3.simplifica())         # -13/5
