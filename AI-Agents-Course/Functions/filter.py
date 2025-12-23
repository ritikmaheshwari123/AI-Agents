## filter function constructs an iterator from those elements of iterable for which function returns true.  
## It is used to filter out items from a list(or any iterable) based on a condition provided in the function.

def is_even(n):
    return n % 2 == 0

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_numbers = filter(is_even, lst)
print(list(filtered_numbers))  # Output: [2, 4, 6, 8, 10]

## filter with lambda function
filtered_numbers_lambda = filter(lambda x: x % 2 == 0, lst)
print(list(filtered_numbers_lambda))  # Output: [2, 4, 6, 8, 10]    

## filter with lambda and multiple conditions
filtered_numbers_multiple = filter(lambda x: x % 2 == 0 and x > 5, lst)
print(list(filtered_numbers_multiple))  # Output: [6, 8, 10]

## filter with dictionary to check age
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35},
    {'name': 'David', 'age': 20}
]       
adults = filter(lambda person: person['age'] >= 25, people)
print(list(adults))  # Output: [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]

