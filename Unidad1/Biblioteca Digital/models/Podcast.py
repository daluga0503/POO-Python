from models.RecursoDigital import RecursoDigital
from typing import Dict, Any

class Podcast(RecursoDigital):
    def __init__(self, titulo, autor, anio, num_episodio, tema, duracion_min, feed_url):
        super().__init__(titulo, autor, anio)
        self.__num_episodio = num_episodio
        self.__tema = tema
        self.__duracion_min = duracion_min
        self.__feed_url = feed_url
        self.__tipo = 'Podcast'

    @property
    def num_episodio(self):
        return self.__num_episodio
    
    @num_episodio.setter
    def num_episodios(self, nuevo_num_episodio):
        if isinstance(nuevo_num_episodio, (int, float)) and nuevo_num_episodio > 0:
            self.__num_episodio = nuevo_num_episodio
        else:
            print('Error: El número de episodios debe de ser un número entero positivo.')

    @property
    def tema(self):
        return self.__tema
    
    @tema.setter
    def tema(self, nuevo_tema):
        if isinstance(nuevo_tema, str) and nuevo_tema:
            self.__tema = nuevo_tema
        else:
            print('Error: El tema debe de ser una cadena que no este vacía.')

    @property
    def duracion_min(self):
        return self.__duracion_min
    
    @duracion_min.setter
    def duracion_min(self, nueva_duracion_min):
        if isinstance(nueva_duracion_min, int) and nueva_duracion_min > 0:
            self.__duracion_min = nueva_duracion_min

    @property
    def feed_url(self):
        return self.__feed_url
    
    @feed_url.setter
    def feed_url(self, nueva_feed_url):
        if isinstance(nueva_feed_url, str) and nueva_feed_url != '':
            self.__feed_url = nueva_feed_url

    def abrir(self):
        return f'Iniciando la reproducción del Poscast {self.titulo} sobre el tema de {self.__tema}\nNº Episodio: {self.__num_episodio} ccon una duración de {self.__duracion_min} minutos. La url es: {self.__feed_url} '


    def tipo(self):
        return 'Podcast'
    
    def __str__(self):
        return f'Titulo: {self.titulo}. Autor: {self.autor}. AÑo: {self.anio}. Nº Epidsodio: {self.num_episodio}. Tema: {self.tema}. Duración Min: {self.duracion_min}. Feed_Url: {self.feed_url}.'
    
    def to_dict(self) -> Dict[str, Any]:
        diccionario_podcast = super().to_dict()
        diccionario_podcast.update({
            "num_episodio": self.__num_episodio,
            "tema": self.__tema,
            "duracion_min": self.__duracion_min,
            "feed_url": self.__feed_url,
            "tipo": self.__tipo
        })
        return diccionario_podcast

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Podcast":
        return Podcast(
            titulo = data["titulo"],
            autor = data["autor"],
            anio = data["anio"],
            num_episodio = data["num_episodio"],
            tema = data["tema"],
            duracion_min = data["duracion_min"],
            feed_url = data["feed_url"]
        )
