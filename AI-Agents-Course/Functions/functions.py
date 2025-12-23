## A function is a block of reusable code that performs a specific task.
## Functions help to organize code, improve readability, and avoid repetition.

##Syntax of a function in Python:
def function_name(parameters):
    """Docstring: Describe what the function does."""
    # Function body: Code to be executed
    return result  # Optional: Return a value   

## Default Parameters
def greet(name="Guest"):
    print(f"hello {name}")

greet("Ritik")
greet()  # Uses default parameter

### Variable length arguments
## Positional arguments

def print_numbers(*args):
    for number in args:
        print(number)

print_numbers("Maheshwari",1, 2, 3, 4, 5)

## Keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Ritik", age=21, city="New York")

## both together
def mixed_args(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

mixed_args(1, 2, 3, name="Ritik", age=21, city="New York")

## multiple return values
def calculate(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result   

sum_val, prod_val = calculate(5, 10)
print(f"Sum: {sum_val}, Product: {prod_val}")