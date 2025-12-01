class Calificacion():
    def __init__(self, modulo, notaFinal = 0.0):
        self.modulo = modulo
        self.notaFinal = notaFinal
    
    def getModulo(self):
        return self.modulo
    
    def getNotaFinal(self):
        return self.notaFinal
    
    def setNotaFinal(self, nota):
        if 0 <= nota <= 10:
            self.notaFinal = nota

    def __str__(self):
        return f"{self._modulo.getNombre()}: {self._notaFinal}"