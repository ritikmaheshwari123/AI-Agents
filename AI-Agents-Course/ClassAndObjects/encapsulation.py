### Enacapsulation with Getter and Setter Methods
## public, protected, and private attributes

class Person:
    def __init__(self, name, age):
        self.name = name          # public attribute
        self._age = age          # protected attribute
        self.__ssn = "123-45-6789"  # private attribute

    # Getter for private attribute
    def get_ssn(self):
        return self.__ssn

    # Setter for private attribute
    def set_ssn(self, ssn):
        self.__ssn = ssn

# Creating an instance of Person
person = Person("Alice", 30)
print("Name (public):", person.name)          # Accessing public attribute
print("Age (protected):", person._age)        # Accessing protected attribute (conventionally)
print("SSN (private via getter):", person.get_ssn())  # Accessing private attribute via getter

class NewPerson(Person):
    def display_info(self):
        print("Name:", self.name)          # Accessing public attribute
        print("Age:", self._age)          # Accessing protected attribute
        # print("SSN:", self.__ssn)       # This would raise an AttributeError
        print("SSN (private via getter):", self.get_ssn())  # Accessing private attribute via getter

# Creating an instance of NewPerson
new_person = NewPerson("Bob", 25)
new_person.display_info()
