class Person:
    def __init__(self,name,age,address,email):
        self.name = name
        self.age = age
        self.address = address
        self.email = email

    def talks(self):
        print(f"{self.name} talks")

    def walks(self):
        print(f"{self.name} is walking")

        
# #person1 object      
# person1 = Person("Mike",24,'Karen','mike@mail.com')
# print(type(person1))
# print(person1.address)
# person1.talks()
# person1.walks()


# #person2 object
# person2 = Person("Kate",21,'Eastleigh','kate@mail.com')
# print(type(person2))
# print(person2.name)
# person2.talks()
# person2.walks()


class Car:
    def __init__(self, brand, model, year, fuel_capacity):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.fuel_level = 0
        self.is_running = False  
    
    def start(self):
        if self.fuel_level > 0:
            self.is_running = True
            return f"{self.brand} {self.model} has started."
        return "Cannot start. No fuel."

    def stop(self):
        self.is_running = False
        return f"{self.brand} {self.model} has stopped."

    def refuel(self, amount):
        if amount <= 0:
            return "Invalid fuel amount"

        if self.fuel_level + amount > self.fuel_capacity:
            self.fuel_level = self.fuel_capacity
            return "Tank is full"

        self.fuel_level += amount
        return f"Refueled {amount}L. Current fuel: {self.fuel_level}L"
    
    def drive(self, distance):
        if not self.is_running:
            return "Start the car first"

        fuel_needed = distance * 0.1  

        if fuel_needed > self.fuel_level:
            return "Not enough fuel to drive that distance"

        self.fuel_level -= fuel_needed
        return f"Drove {distance}km. Fuel left: {self.fuel_level}L"


    def display_car_info(self):
        return f"""
Brand: {self.brand}
Model: {self.model}
Year: {self.year}
Fuel Capacity: {self.fuel_capacity}
Fuel Level: {self.fuel_level}
Is Running: {self.is_running}
"""
car = Car("Toyota", "Corolla", 2020, 50)

# print(car.display_car_info())

# print(car.start())
# print(car.drive(50))
# print(car.refuel(10))
# print(car.drive(100))
# print(car.stop())

# print(car.display_car_info())

from datetime import datetime

today = datetime.now()
print(today)


class BankAccount:
    def __init__(self, account_number, balance, name, date_opened=today):
        self.account_number = account_number
        self.balance = balance
        self.name = name
        self.date_opened = date_opened

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount,cannot complete deposit")
        self.balance = self.balance + amount
        print(f"{self.name} deposited {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount
            print(f"{self.name} withdrew {amount}")

    def display_info(self):
        print(f"Acc no:{self.account_number} - Balance: {self.balance} -- Date Opened:{self.date_opened}")


# bankaccount1 
bankAccount1 = BankAccount("88210", 1000, "Mike")

# bankaccount2 
bankAccount2 = BankAccount("88211", 500, "Kate")

bankAccount1.deposit(1000)
bankAccount1.withdraw(5000)
bankAccount1.display_info()

# bankAccount2.deposit()
# bankAccount2.withdraw()
# bankAccount2.display_info()




