from Alumno import Alumno
from Modulo import Modulo as mod
from datetime import date

m1 = mod("Programación", 100)
m2 = mod("Bases de Datos", 80)
m3 = mod("Sistemas", 60)

a1 = Alumno("12345678A", "Juan", "Pérez", date(2002, 5, 15), "DAM")

a1.matricular(m1)
a1.matricular(m2)
a1.matricular(m3)

a1.calificar(m1, 7)
a1.calificar(m2, 4)
a1.calificar(m3, 8)

print(a1)
print(a1.ciclo)
print("Promociona:", a1.promociona())