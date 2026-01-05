## function copy

def welcome():
    return "Welcome to advance Python concepts!"

wel = welcome()
print(wel)

## Closures

def main_welcome(msg):
    def sub_welcome_method():
        print("Welcome to advance Python concepts!")
        print(msg)
        print("Understanding closures in Python0")
    return sub_welcome_method()

main_welcome("This is a message passed to the inner function.")

def main_welcome_func(func):
    def sub_welcome_method():
        print("Welcome to advance Python concepts!")
        func()
        print("Understanding closures in Python0")
    return sub_welcome_method()

main_welcome_func(print)

def main_welcome_len(func,lst):
    def sub_welcome_method():
        print("Welcome to advance Python concepts!")
        print(func(lst))
        print("Understanding closures in Python0")
    return sub_welcome_method()

main_welcome_len(len,[1,2,3,4,5])

## Decorators

@main_welcome_func  
def decorated_welcome():
    print("This is a decorated welcome function.")