# 1. Classes & Objects
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display(self):
        print(f"{self.brand} - {self.year}")

car1 = Car("Toyota", 2020)
car2 = Car("Tesla", 2023)
car1.display()
car2.display()

# 2. Inheritance
class ElectricCar(Car):
    def __init__(self, brand, year, battery_size):
        super().__init__(brand, year)
        self.battery_size = battery_size

    def display(self):
        print(f"{self.brand} - {self.year}, Battery: {self.battery_size}kWh")

ecar = ElectricCar("Tesla", 2023, 75)
ecar.display()

# 3. Encapsulation
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # private attribute

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

account = BankAccount("Lloyd")
account.deposit(500)
print(account.get_balance())

# 4. Exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# 5. File Handling
with open("employees.txt", "w") as f:
    f.write("Name: Lloyd, Role: AI Engineer\n")

with open("employees.txt", "r") as f:
    print(f.read())
