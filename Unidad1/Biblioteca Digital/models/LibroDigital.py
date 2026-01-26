from models.RecursoDigital import RecursoDigital
from typing import Dict, Any

class LibroDigital(RecursoDigital):
    def __init__(self, titulo, autor, anio, num_paginas, formato, isbn):
        super().__init__(titulo, autor, anio)
        self.__num_paginas = num_paginas
        self.__formato = formato
        self.__isbn = isbn
        self.__tipo = 'LibroDigital'


    @property
    def num_paginas(self):
        return self.__num_paginas
    
    @num_paginas.setter
    def num_paginas(self, nuevo_num_paginas):
        if isinstance(nuevo_num_paginas, int) and nuevo_num_paginas > 0 :
            self.__num_paginas = nuevo_num_paginas
        else:
            print('Error: El número de las páginas debe ser un número entero positivo')

    @property
    def formato(self):
        return self.__formato
    
    @formato.setter
    def formato(self, nuevo_formato):
        if isinstance(nuevo_formato, str) and nuevo_formato:
            self.__formato = nuevo_formato
        else:
            print('Error: El formato debe ser una cadena que no este vacía.')

    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, nuevo_isbn):
        if isinstance(nuevo_isbn, str) and nuevo_isbn != '':
            self.__isbn = nuevo_isbn

    def abrir(self):
        pass

    def tipo(self):
        pass

    
    def __str__(self):
        return f'Titulo: {self.titulo}. Autor: {self.autor}. Año: {self.anio}. Nº Páginas: {self.num_paginas}. Formato: {self.formato}. ISBN: {self.isbn}.'
    
    
    def to_dict(self) -> Dict[str, Any]:
        diccionario_libro = super().to_dict()
        diccionario_libro.update({
            "num_paginas": self.__num_paginas,
            "formato": self.__formato,
            "isbn": self.__isbn,
            "tipo": self.__tipo
        })
        return diccionario_libro
        
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "LibroDigital":
        return LibroDigital(
            titulo = data["titulo"], 
            autor = data["autor"], 
            anio = data["anio"], 
            num_paginas = data["num_paginas"], 
            formato = data["formato"], 
            isbn = data["isbn"]
        )