class Point():
    def __init__(self, x, y, constante):
        self.x = x
        self.y = y
        self.constante = constante
    
    def __str__(self):
        return f'X: {self.x} Y: {self.y} Constante: {self.constante}'
    

p1 = Point(4,4,1)
print(p1.__str__())