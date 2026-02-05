
from typing import List, Dict
from models.House import House
import json, os

def lectura_recursos(ruta, n_items = 10) -> List[House]:
    if not os.path.exists(ruta):
        raise FileNotFoundError(f'No se ha encontrado el archivo en: {ruta}.')

    with open(ruta, 'r') as file:
        contenido = json.load(file)

        if not isinstance(contenido, List):
            raise ValueError('El contenido de json debe ser una lista.')
        
        recursos = []

        for item in contenido[:n_items]:
            if isinstance(item, Dict):
                recursos.append(House.from_dict(item))
            else:
                raise ValueError('El contenido debe estar en formato diccionario.')
        return recursos
    

def escritura_recurso(ruta, contenido: House) -> bool:

    if not os.path.exists(ruta):
        raise FileNotFoundError(f'No se ha encontrado el archivo en: {ruta}.')

    datos = []
    if os.path.exists(ruta) and os.path.getsize(ruta) > 0:
        with open(ruta, 'r', encoding='utf-8') as file:
            datos = json.load(file) # Cargamos la lista completa
    
    # 2. Añadir la nueva casa (convertida a diccionario)
    datos.append(contenido.to_dict())
    
    try:
        # 3. Sobrescribir el archivo ('w') con la lista completa actualizada
        with open(ruta, 'w', encoding='utf-8') as file:
            json.dump(datos, file, indent=4)
        return True
    except Exception as e:
        return False