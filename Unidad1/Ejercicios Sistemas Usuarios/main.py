from Alumno import Alumno
from Profesor import Profesor


alumno1 = Alumno('Alumno1', 'alumno1@gmail.com', '1º DAM', 8.5)
alumno2 = Alumno('Alumno2', 'alumno2@gmail.com', '1º ASIR', 7)
alumno3 = Alumno('Alumno3', 'alumno3@gmail.com', '1º DAW', 9.5)

profesor1 = Profesor('Profesor1', 'profesor1@gmail.com', 'Base de datos')
profesor2 = Profesor('Profesor2', 'profesor2@gmail.com', 'Programación')
profesor3 = Profesor('Profesor3', 'profesor3@gmail.com', 'Diseño Web')

lista_usuarios = [alumno1, alumno2, alumno3, profesor1, profesor2, profesor3]

for usuario in lista_usuarios:
    print(usuario.presentacion())