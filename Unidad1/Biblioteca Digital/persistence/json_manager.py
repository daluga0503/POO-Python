from __future__ import annotations
import json, os
from typing import List
from models.RecursoDigital import RecursoDigital

def guardar_recursos(ruta_fichero:str, recursos: List[RecursoDigital]) -> None:
    data = [recurso.to_dict() for recurso in recursos]
    os.makedirs(os.path.dirname(ruta_fichero), exist_ok=True)

    with open(ruta_fichero, 'w') as file:
        json.dump(data, file, indent=2)

def cargar_recursos(ruta_fichero: str) -> List[RecursoDigital]:
    if not os.path.exists(ruta_fichero):
        return []
    
    with open(ruta_fichero, 'r') as file:
        contenido = json.load(file)

    if not isinstance(contenido, list):
        raise ValueError('El json debe contener una lista de recursos.')
    
    recursos = List[RecursoDigital] = []

    for item in contenido:
        if not isinstance(item, dict):
            raise ValueError('El item debe ser un objeto diccionario.')   
        recursos.append(RecursoDigital.from_dict(item))

    return recursos