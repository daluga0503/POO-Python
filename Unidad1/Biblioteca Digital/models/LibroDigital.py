from models.RecursoDigital import RecursoDigital
from typing import Dict, Any

class LibroDigital(RecursoDigital):
    def __init__(self, titulo, autor, anio, num_paginas, formato):
        super().__init__(titulo, autor, anio)
        self.num_paginas = num_paginas
        self.formato = formato

    def get_num_paginas(self):
        return self.num_paginas
    
    def set_num_paginas(self, nuevo_num_paginas):
        if isinstance(nuevo_num_paginas, int) and nuevo_num_paginas > 0 :
            self.num_paginas = nuevo_num_paginas
        else:
            print('Error: El número de las páginas debe ser un número entero positivo')

    def get_formato(self):
        return self.formato
    
    def set_formato(self, nuevo_formato):
        if isinstance(nuevo_formato, str) and nuevo_formato:
            self.formato = nuevo_formato
        else:
            print('Error: El formato debe ser una cadena que no este vacía.')

    def abrir(self):
        return f'Abriendo el libro {self.get_titulo()} en formato {self.get_formato()}'
    
    def tipo(self):
        return 'Libro'
    
    def to_dict(self) -> Dict[str, Any]:
        diccionario_libro = super().to_dict()
        diccionario_libro.update({
            "paginas": self.num_paginas,
            "formato": self.formato
        })
        return diccionario_libro
        
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "LibroDigital":
        return LibroDigital(
            data["recurso_id"], data["titulo"], data["autor"], data["anio"], data["num_paginas"], data["formato"], data["isbn"]
        )
        