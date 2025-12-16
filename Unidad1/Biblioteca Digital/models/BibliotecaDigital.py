from RecursoDigital import RecursoDigital

class BibliotecaDigital():
    def __init__(self):
        self.__recursos = []

    def anyadir_recurso(self, recurso):
        if isinstance(recurso, RecursoDigital):
            self.__recursos.append(recurso)
            print(f'Recurso Añadido: {recurso.get_titulo()} ({recurso.tipo()})')
        else:
            print('Error: Solo se pueden añadir instancias de RecursoDigital.')

    def listar_recursos(self):
        if len(self.__recursos) != 0:
            for i, recurso in enumerate(self.__recursos):
                print(f'{i+1} Tipo: {recurso.tipo()} | {recurso.descripcion_basica()}\n')
        else:
            return 'La biblioteca esta vacía'
        
    
    def abrir_todos(self):
        if len(self.__recursos) != 0:
            for recurso in self.__recursos:
                print(f'> {recurso.abrir()}')
        else:
            return 'La biblioteca esta vacía'