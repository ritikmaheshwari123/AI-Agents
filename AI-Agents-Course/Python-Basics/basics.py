## Syntax and Semantics in Python

'''
Syntax refers to the set of rules that define the combination of symbols that are considered to be correctly structured programs in that language. 
In simple terms, syntax is about the correct arrangement of words and symbols in a code
'''

'''
Semantics refers to the meaning of the interpretation of the symbols, characters and commands in a programming language.
It is about what the code is supposed to do when it is executed.
'''


## Case Sensitivity - Python is a case-sensitive programming language.
name="Ritik"
Name="Maheshwari"

print(name)
print(Name)

## Indentation
## Python uses indentation to define blocks of code. Consistent use of spaces (commonly 4 spaces) or tabs is required.

age = 18
if age >= 18:
    print("You are an adult.")


## Comments
# This is a single-line comment

'''
This is a multi-line comment
which spans multiple lines. 
'''

## Line Continuation

total = 1 + 2 + 3 + \
        4 + 5
print(total)

## Multiple Statements in a Single Line
a = 5; b = 10; c = a + b
print(c)

## Understand Semantics in Python
# Varibale Assignment
var = 25  # integer

# Type refrence
type_age = type(var); print(type_age)
var = "Ritik"  # string
type_name = type(var); print(type_name)
