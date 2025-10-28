from Persona import Persona
from Calificacion import Calificacion

class Alumno(Persona):
    def __init__(self, dni, nombre, apellidos, fechaNacimiento ,ciclo):
        super().__init__(dni, nombre, apellidos, fechaNacimiento)
        self.ciclo = ciclo
        self.calificaciones = []

    def matricular(self, modulo):
        for calificacion in self.calificaciones:
            if calificacion.getModulo() == modulo.getNombre():
                return
        self.calificaciones.append(Calificacion(modulo, 0))


    def calificar(self, modulo, nota):
        for calificacion in self.calificaciones:
            if calificacion.getModulo().getNombre() == modulo.getNombre():
                calificacion.setNotaFinal(nota)
                return

    
    def promociona(self):
        if not self.calificaciones:
            return False
        total_horas = sum(calificacion.getModulo().getHoras() for calificacion in self.calificaciones)
        horas_aprobadas = sum(calificacion.getModulo().getHoras() for calificacion in self.calificaciones if calificacion.getNotaFinal() >= 5)
        return horas_aprobadas >= total_horas / 2
    
    def getNotaMedia(self):
        if not self.calificaciones:
            return 0.0
        suma = sum(calificacion.getNotaFinal() for calificacion in self.calificaciones)
        return suma / len(self.calificaciones)

    def __str__(self):
        return f'{super().__str__()}, Ciclo: {self.ciclo}, Nota Media: {self.getNotaMedia():.2f}'
    


    

        
