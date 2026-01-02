class Car:
    pass

audi = Car()
bmw = Car()

print(type(audi))
print(type(bmw))

class Dog:
    ## constructor
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Buddy", 3)
dog1.bark()

### Modeliing a bank account
class BankAccount:  
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.") 
    
    def get_balance(self):
        print(f"Current balance is {self.balance}.")

account = BankAccount("Alice", 1000)
account.deposit(500)    
account.withdraw(200)
account.get_balance()
account.withdraw(2000)
