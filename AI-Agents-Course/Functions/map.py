## map applies a given function to all items in an iterable (like a list) and returns a map object (which is an iterator).

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# You can also use a defined function with map
def increment(x):
    return x + 1
incremented_numbers = map(increment, numbers)
print(list(incremented_numbers))  # Output: [2, 3, 4, 5, 6] 

# map can be used with multiple iterables as well
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
summed_numbers = map(lambda x, y: x + y, numbers1, numbers2)
print(list(summed_numbers))  # Output: [5, 7, 9]

# Note: The map object is an iterator, so it can only be traversed once. To reuse the results, convert it to a list or another collection type.

## map to convert list of strings to integers
string_numbers = ['1', '2', '3', '4', '5']
int_numbers = map(int, string_numbers)
print(list(int_numbers))  # Output: [1, 2, 3, 4, 5]

words = ['hello', 'world', 'python']
uppercased_words = map(str.upper, words)
print(list(uppercased_words))  # Output: ['HELLO', 'WORLD', 'PYTHON']

## map on list of dictionaries to extract a specific key's value
people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
names = map(lambda person: person['name'], people)
print(list(names))  # Output: ['Alice', 'Bob', 'Charlie']


