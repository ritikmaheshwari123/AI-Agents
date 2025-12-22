## Unordered collection of key-value pairs
## Key must be unique and immutable

empty_dict = {}
another_empty_dict = dict()

# Creating a dictionary
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

print("Original Dictionary:", my_dict)
# Accessing values
print("Name:", my_dict['name'])
print("Age:", my_dict.get('age'))   

## Duplicate keys will overwrite previous values
my_dict['age'] = 31
print("Updated Age:", my_dict['age'])

print(my_dict.get("lastname"))

# Adding a new key-value pair
my_dict['profession'] = 'Engineer'
print("After Adding Profession:", my_dict)

# Removing a key-value pair
del my_dict['city']
print("After Deleting City:", my_dict)
removed_value = my_dict.pop('age')
print("After Popping Age:", my_dict)
print("Popped Age Value:", removed_value)

## Dictionary Methods
# keys(), values(), items()
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

## shallow copy 
my_dict_copy = my_dict
print(my_dict)
print(my_dict_copy)

my_dict['hobby'] = 'painting'
print("Original Dictionary after modification:", my_dict)
print("Copy after original modification:", my_dict_copy)

my_dict_shallow_copy = my_dict.copy()
my_dict['favorite_color'] = 'blue'
print("Original Dictionary after adding favorite_color:", my_dict)
print("Shallow Copy after original modification:", my_dict_shallow_copy)

## Iterating through a dictionary
# Iterating through keys
for key in my_dict:
    print("Key:", key)
# Iterating through values
for value in my_dict.values():
    print("Value:", value)
# Iterating through key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")

 ## Nested Dictionaries
nested_dict = {
    'person1': {
        'name': 'Bob',
        'age': 25
    },
    'person2': {
        'name': 'Carol',
        'age': 28
    }       
}
print("Nested Dictionary:", nested_dict)
print("Person1's Name:", nested_dict['person1']['name'])

## iteratimng through nested dictionary
for person, details in nested_dict.items():
    print(f"{person}:")
    for key, value in details.items():
        print(f"  {key}: {value}")

## Dictionary Comprehension
squares = {x: x**2 for x in range(5)}
print("Squares Dictionary:", squares)

## conditional dictionary comprehension
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print("Even Squares Dictionary:", even_squares) 

## Merging Dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary:", merged_dict)



