
from typing import List, Dict
from models.House import House
import json, os

def lectura_recursos(ruta, n_items = 10) -> List[House]:
    if not os.path.exists(ruta):
        raise FileNotFoundError(f'No se ha encontrado el archivo en: {ruta}.')

    with open(ruta, 'r') as file:
        contenido = json.load(ruta)

        if not isinstance(List, contenido):
            raise ValueError('El contenido de json debe ser una lista.')
        
        recursos = List[House] = []

        for item in contenido[:n_items]:
            if isinstance(Dict, item):
                recursos.append(House.from_dict(item))
            else:
                raise ValueError('El contenido debe estar en formato diccionario.')
        return recursos
    

def escritura_recurso(ruta, contenido: House) -> None:
    if not os.path.exists(ruta):
        raise FileNotFoundError(f'No se ha encontrado el archivo en: {ruta}.')

    with open(ruta, 'a') as file:
        json.dump(House.to_dict(contenido), file, indent=2)