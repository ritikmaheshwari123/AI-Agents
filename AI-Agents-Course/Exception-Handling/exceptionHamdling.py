## Exception try and except block

try:
    a=b
    result = 10 / 0
except NameError as ex:
    print(ex)
except Exception as ex:
    print("Some other exception occurred:", ex)

## try,except.else block

try:
    result = 10 / 2
except Exception as ex:
    print("Some exception occurred:", ex)
else:
    print("The result is:", result)

## try,except,else,finally block

try:
    result = 10 / 2
except Exception as ex:
    print("Some exception occurred:", ex)
else:
    print("The result is:", result)
finally:
    print("Execution completed.")

## file handling with exception
try:
    file = open("non_existent_file.txt", "r")
    content = file.read()
except FileNotFoundError as ex:
    print("File not found:", ex)
finally:
    try:
        file.close()
    except:
        pass
    print("File operation completed.")  
