class Calificacion():
    def __init__(self, modulo, notaFinal = 0.0):
        self.modulo = modulo
        self.notaFinal = notaFinal
    
    def getModulo(self):
        return self.modulo
    
    def getNotaFinal(self):
        return self.notaFinal
    
    def setNotaFinal(self, nota):
        self.notaFinal = nota