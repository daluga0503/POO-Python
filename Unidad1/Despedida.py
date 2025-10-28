class Despedida():
    def __init__(self, nombre, hora):
        self.nombre = nombre
        self.hora = hora

    def mostar_despedida(self):
        if self.hora > 12:
            print(f'Que tengas una excelente mañana, {self.nombre}')
        elif self.hora >= 12 and self.hora < 21:
            print(f'Que tengas una buena tarde, {self.nombre}')
        else:
            print(f'Que tengas una buena noche, {self.nombre}')
    
    @classmethod
    def desde_texto(cls, texto):
        texto = texto.split(',')
        try:
            int(texto[1])
            return cls(texto[0], texto[1])
        except:
            raise ValueError('Error al crear la instancia del objeto Despedida')
    
    @staticmethod
    def es_hora_valida(hora):
        return hora >= 0 and hora <= 23
    

despedida1 = Despedida('Juan', 12)
despedida1.mostar_despedida()
despedida2 = Despedida.desde_texto('Daniel,12')
print(Despedida.es_hora_valida(-1))