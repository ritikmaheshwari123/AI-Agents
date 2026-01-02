## Method overriding example in Python
class Animal:
    def speak(self):
        return "Sound of a generic animal"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!

## Polymorphism with functions and methods
class Shape:
    def area(self):
        print("Area of generic shape")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
def print_area(shape):
    print("Area:", shape.area())
rect = Rectangle(4, 5)
circle = Circle(3)
print_area(rect)   # Output: Area: 20
print_area(circle) # Output: Area: 28.26

## polymorphism with abstract base classes

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"

def vehicle_start(vehicle):
    print(vehicle.start_engine())
car = Car()
motorcycle = Motorcycle()
vehicle_start(car)         # Output: Car engine started
vehicle_start(motorcycle)  # Output: Motorcycle engine started
