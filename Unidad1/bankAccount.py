class BankAccount():

    def __init__(self):
        self.name = ""
        self.balance = 0

    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance

    def  display(self):
        print(f'Name: {self.name}\nBalance: {self.balance}')

    def recall(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance +=amount

cuenta1 = BankAccount()
cuenta2 = BankAccount()

cuenta1.set_details('Cuenta 1', 1000)
cuenta2.set_details('Cuenta 2', 500)

cuenta1.display()
cuenta2.display()

cuenta1.recall(100)
cuenta1.display()

cuenta1.deposit(200)
cuenta1.display()