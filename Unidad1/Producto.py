class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        if porcentaje >=0 and porcentaje <= 100:
            self.precio = round(self.precio - ((porcentaje * self.precio) / 100), 2)
            return f'Se ha le ha aplicado un {porcentaje}% de descuento al producto: {self.nombre}, su nuevo precio es: {self.precio}'
        else:
            return 'Error al aplicar el descuento'

    @classmethod
    def desde_texto(cls, texto):
        producto = texto.split(',')
        try:
            producto[1] = float(producto[1])
            return cls(producto[0], producto[1])
        except:
            raise ValueError('Error al introducir el precio del producto')

    @staticmethod
    def es_precio_valido(precio):
        return precio >= 0
        

prod1 = Producto('Camiseta', 25.99)
print(prod1.aplicar_descuento(20))
prod2 = Producto.desde_texto('Pantalón, 25.55')
print(Producto.es_precio_valido(15))