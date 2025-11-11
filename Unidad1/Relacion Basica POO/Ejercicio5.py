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


    def invierte(self):
        if self.nominador == 0:
            return ZeroDivisionError('No se puede invertir una fracción con numerador 0')
        return Fraccion(self.denominador, self.numerador)
    
    def simplifica(self):
        pass
    def multiplica(self):
        pass
    def divide(self):
        pass
