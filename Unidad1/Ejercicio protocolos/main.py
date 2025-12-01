from Libro import Libro
from Revista import Revista

libro1 = Libro("123-456", "El Quijote", 1605)
revista1 = Revista("789-101", "National Geographic", 2025, 11)

print(libro1)
print(revista1)
# Probamos el protocolo Prestable
libro1.presta()
print("¿Está prestado?", libro1.estaPrestado())
libro1.devuelve()
print("¿Está prestado?", libro1.estaPrestado())