class Modulo():
    def __init__(self, nombre, horas):
        self.nombre = nombre
        self.horas = horas

    def getNombre(self):
        return self.nombre
    
    def getHoras(self):
        return self.horas
    
    def __str__(self):
        return f'Nombre del módulo: {self.nombre}, horas: {self.horas}'