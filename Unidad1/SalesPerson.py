class SalesPerson():
    total_revenue = 0
    names = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sales_amount = 0
        SalesPerson.names.append(name)

    
    def make_sale(self, money):
        self.sales_amount += money
        SalesPerson.total_revenue += self.sales_amount

    def show(self):
        print(self.name, self.age, self.sales_amount)


s1 = SalesPerson('Alumno 1', 25)
s2 = SalesPerson('Alumno 2', 22)
s3 = SalesPerson('Alumno 3', 27)
s1 = SalesPerson('Alumno 4', 25)
s2 = SalesPerson('Alumno 5', 22)
s3 = SalesPerson('Alumno 6', 27)
s1 = SalesPerson('Alumno 7', 25)
s2 = SalesPerson('Alumno 8', 22)
s3 = SalesPerson('Alumno 9', 27)
s1 = SalesPerson('Alumno 10', 25)
s2 = SalesPerson('Alumno 11', 22)
s3 = SalesPerson('Alumno 12', 27)
 
s1.make_sale(1000)
s1.make_sale(1200)
s2.make_sale(5000)
s3.make_sale(3000)
s3.make_sale(8000)
 
s1.show()
s2.show()
s3.show()
print(f'Personas agregadas: {SalesPerson.names}')
print(f'Total ganacias: {SalesPerson.total_revenue}')
