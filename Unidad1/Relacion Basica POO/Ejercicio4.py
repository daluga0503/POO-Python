"""
Crea las clases Animal, Mamifero, Ave, Gato, Perro, Canario, Pinguino y Lagarto. 
Crea, al menos, tres métodos específicos de cada clase y redefine el/los método/s cuando sea necesario. 
Prueba las clases creadas en un programa en el que se instancien objetos y se les apliquen métodos.

Estoy comiendo palomitas
Soy un pingüino programador, estoy programando en Java
Zzzzzzz
Toma mi patita
Toma pecho, hazte grande
Estoy cuidando mis crias
Estoy tomando el Sol
Zzzzzzz
"""
class Animal():
    def comer(self):
        print("Estoy comiendo...")

    def dormir(self):
        print("Zzzzzzz...")

    def mover(self):
        print("Me estoy moviendo...")


class Mamifero(Animal):
    def amamantar(self):
        print("Toma pecho, hazte grande")

    def cuidar_crias(self):
        print("Estoy cuidando mis crias")

    def mover(self):
        print("Me muevo caminando o corriendo")


class Ave(Animal):
    def volar(self):
        print("Estoy volando")

    def poner_huevos(self):
        print("He puesto un huevo")

    def mover(self):
        print("Me muevo volando o saltando")


class Gato(Mamifero):
    def maullar(self):
        print("Miau!")

    def sacar_garras(self):
        print("Saco mis garras")

    def ronronear(self):
        print("Prrrr...")


class Perro(Mamifero):
    def ladrar(self):
        print("Guau!")

    def traer_pelota(self):
        print("Traigo la pelota")

    def dar_patita(self):
        print("Toma mi patita")


class Canario(Ave):
    def cantar(self):
        print("Pío pío pío")

    def picotear(self):
        print("Estoy picoteando semillas")

    def saltar(self):
        print("Estoy saltando en la jaula")


class Pinguino(Ave):
    def nadar(self):
        print("Estoy nadando en aguas frías")

    def programar(self):
        print("Soy un pingüino programador, estoy programando en Python")

    def volar(self):
        print("No puedo volar, pero camino y nado")


class Lagarto(Animal):
    def tomar_sol(self):
        print("Estoy tomando el Sol")

    def cambiar_color(self):
        print("Cambio el color de mi piel")

    def reptar(self):
        print("Me desplazo reptando")


if __name__ == "__main__":
    gato = Gato()
    perro = Perro()
    canario = Canario()
    pinguino = Pinguino()
    lagarto = Lagarto()

    # Probando métodos
    gato.comer()
    gato.maullar()
    gato.ronronear()

    perro.ladrar()
    perro.dar_patita()
    perro.cuidar_crias()

    canario.cantar()
    canario.volar()
    canario.poner_huevos()

    pinguino.nadar()
    pinguino.programar()
    pinguino.volar()

    lagarto.tomar_sol()
    lagarto.cambiar_color()
    lagarto.dormir()
