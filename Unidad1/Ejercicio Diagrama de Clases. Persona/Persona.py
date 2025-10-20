class Persona():
    def __init__(self, dni, nombre, apellidos, fechaNacimiento):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.fechaNacimiento = fechaNacimiento

    def getDni(self):
        return self.dni
    
    def getNombre(self):
        return self.nombre
    
    def getFechaNacimiento(self):
        return self.fechaNacimiento
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Apellidos: {self.apellidos}, DNI: {self.dni}, Fecha Nacieminto: {self.fechaNacimiento}'
    