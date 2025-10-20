import Persona
import Modulo
import Calificacion

class Alumno(Persona):
    def __init__(self, dni, nombre, apellidos, fechaNacimiento ,ciclo, calificaciones):
        super().__init__(dni, nombre, apellidos, fechaNacimiento)
        self.ciclo = ciclo
        self.calificaciones = calificaciones

    def matricular(self, modulo):
        cali = Calificacion(modulo)
        for modulo in self.calificaciones:
            if modulo == cali.getModulo()


    def calificar(self, modulo, nota):

    
    def promociona(self):

    def getNotaMedia(self):

    def __str__(self):

    


    

        
