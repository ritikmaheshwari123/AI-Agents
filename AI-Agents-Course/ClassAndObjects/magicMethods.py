'''
__init__ : Initializes a new instance of a class.
__str__ : Returns a string representation of the object for human-readable output.
__repr__ : Returns a official string representation of the object for debugging and development.
__len__ : Returns the length of the object.
__getitem__ : Retrieves an item from the object using indexing.
__setitem__ : Sets an item in the object using indexing.
'''

class Person:
    def __init__(self, name="John Doe", age=30):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"

    def __len__(self):
        return len(self.name)

    def __getitem__(self, index):
        return self.name[index]

    def __setitem__(self, index, value):
        name_list = list(self.name)
        name_list[index] = value
        self.name = ''.join(name_list)

person = Person()
print(dir(person))  # Lists all attributes and methods of the Person class instance
print(person)       # Uses __str__ method
print(repr(person)) # Uses __repr__ method
print(len(person))  # Uses __len__ method
print(person[0])    # Uses __getitem__ method
person[0] = 'J'    # Uses __setitem__ method
print(person.name)  # Check the updated name after using __setitem__


