# Declaring and assigning variables

age=26 #integer variable
height=5.8 #float variable
name="Ritik Maheshwari" #string variable
is_student=True #boolean variable

# Printing the variables
print("Name:", name)        
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)


# Naming conventions
# variable names should be descriptive
# must start with a letter or underscore and can contain letters, digits, and underscores
# variable names are case-sensitive

# valid variable names
first_name = "Ritik"
last_name = "Maheshwari"

age=26
print(type(age))  # Output: <class 'int'>

# Type conversion
age_str = str(age)  # converting integer to string
print("Age as string:", age_str)
print("Type of age_str:", type(age_str))  # Output: <class 'str'>   

# input from user
user_age = input("Enter your age: ")
print(user_age, type(user_age))  # Output will be of type 'str'

