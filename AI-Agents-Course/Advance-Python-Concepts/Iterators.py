## Iterators allow for efficient looping and memory management in Python.
## It provides a way to access elements of a collection sequentially without exposing the underlying representation.

iterator = iter([1, 2, 3, 4, 5])  # Create an iterator from a list
print(type(iterator))  # Output: <class 'list_iterator'>
print(iterator)  # Output: <list_iterator object at ...>

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
print(next(iterator))  # Output: 4
print(next(iterator))  # Output: 5
# print(next(iterator))  # Raises StopIteration error


