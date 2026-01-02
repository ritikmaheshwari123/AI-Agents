## Single Inheritance Example
class Car:
    def __init__(self, windows, doors, engine_type):
        self.windows = windows
        self.doors = doors
        self.engine_type = engine_type
    
    def drive(self):
        print(f"The car with {self.engine_type} engine is driving.")

car1 = Car(4, 4, "V6")
car1.drive()

class Tesla(Car):
    def __init__(self, windows, doors, engine_type, autopilot):
        super().__init__(windows, doors, engine_type)
        self.autopilot = autopilot
    def enable_autopilot(self):
        if self.autopilot:
            print("Autopilot is enabled.")
        else:
            print("This Tesla does not have autopilot feature.")

tesla1 = Tesla(4, 4, "Electric", True)
tesla1.drive()
tesla1.enable_autopilot()

## Multi-Level Inheritance Example
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Subclass must implement this method.")

class Pet:
    def __init__(self, owner):
        self.owner = owner

class Dog(Animal, Pet):
    def __init__(self, name, owner, breed):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)
        self.breed = breed
    def speak(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Buddy", "Alice", "Golden Retriever")
dog1.speak()
