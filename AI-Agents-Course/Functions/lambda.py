## Lambda functions are small anonymous functions defined with the lambda keyword.
## They can take any number of arguments but can only have one expression.

## Syntax:
lambda arguments: expression

addition = lambda a,b: a + b  # This lambda function takes two arguments and returns their sum.
print("Sum:", addition(5, 3))  # Output: Sum: 8

even = lambda x: x % 2 == 0  # This lambda function checks if a number is even.
print("Is 4 even?", even(4))  # Output: Is 4 even

## map() - applies a function to all items in an input list.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared)  # Output: Squared numbers: [1, 4, 9, 16, 25]
