## Lists arte ordered, mutable (can be changed) collections of items.
## they can contain items of different data types.

lst = []
print(type(lst))  

mixed_list = ["Alice", "Bob", "Charlie",1,2,3.5,True]
print(mixed_list)  

## Accessing elements in a list
Fruits = ["Apple", "Banana", "Cherry", "Date"]
print(Fruits[0])
print(Fruits[-1])
print(Fruits[1:])
print(Fruits[:2])
print(Fruits[1:3])

## Modifying elements in a list
Fruits[1] = "Blueberry"
print(Fruits)

## List methods
Fruits.append("Elderberry")
print(Fruits)   
Fruits.insert(1, "Avocado")
print(Fruits)
Fruits.remove("Date")
print(Fruits)
popped_fruit = Fruits.pop()
print(popped_fruit)
print(Fruits)
Fruits.sort()
print(Fruits)
Fruits.reverse()
print(Fruits)
length = len(Fruits)
print(length)
index = Fruits.index("Cherry")
print(index)
count = Fruits.count("Apple")
print(count)
Fruits.extend(["Fig", "Grape"])
print(Fruits)
Fruits.clear()
print(Fruits)

## Slicing Lists
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers[2:5])
print(numbers[:4])
print(numbers[5:])
print(numbers[-3:])
print(numbers[::2])
print(numbers[::-1])
print(numbers[1:7:3])

## Iterating through a list
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)

## Iterating with index
for index,color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")

## List comprehensions
squared_numbers = [x**2 for x in range(10)] 
print(squared_numbers)

## list comprehension with condition
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)

## Nested Lists comprehension
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
nested_list = [[x, y] for x in lst1 for y in lst2]
print(nested_list)

## List comprehension with function
def square(x):
    return x * x
squared_list = [square(x) for x in range(10)]
print(squared_list)




