from RecursoDigital import RecursoDigital

class Podcast(RecursoDigital):
    def __init__(self, titulo, autor, anio, num_episodios, tema):
        super().__init__(titulo, autor, anio)
        self.num_episodios = num_episodios
        self.tema = tema

    def get_num_episodios(self):
        return self.num_episodios
    
    def set_num_episodios(self, nuevo_num_episodios):
        if isinstance(nuevo_num_episodios, (int, float)) and nuevo_num_episodios > 0:
            self.num_episodios = nuevo_num_episodios
        else:
            print('Error: El número de episodios debe de ser un número entero positivo.')

    def get_tema(self):
        return self.tema
    
    def set_tema(self, nuevo_tema):
        if isinstance(nuevo_tema, str) and nuevo_tema:
            self.nivel = nuevo_tema
        else:
            print('Error: El tema debe de ser una cadena que no este vacía.')


    def abrir(self):
        return f'Iniciando la reproducción del Poscast {self.get_titulo()} sobre el tema de {self.get_tema()}\nNº Episodios: {self.get_num_episodios()}'


    def tipo(self):
        return 'Podcast'