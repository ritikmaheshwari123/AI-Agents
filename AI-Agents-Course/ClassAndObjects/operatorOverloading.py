### common operator overloading magic methods in Python

'''
__add__(self, other)         # Addition operator +
__sub__(self, other)         # Subtraction operator -
__mul__(self, other)         # Multiplication operator *
__truediv__(self, other)      # Division operator /
__eq__(self, other)         # Equality operator ==
__lt__(self, other)         # Less than operator <
'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
v4 = v2 - v1
v5 = v1 * 3
v6 = v2 / 2
print("v3 (Addition):", v3)
print("v4 (Subtraction):", v4)
print("v5 (Multiplication):", v5)
print("v6 (Division):", v6)
print("v1 == v2:", v1 == v2)
print("v1 < v2:", v1 < v2)
