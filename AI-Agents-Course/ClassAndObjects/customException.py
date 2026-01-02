## Custom exception: Raise and throw a user-defined exception

class Error(Exception):
    pass

class doException(Error):
    pass

year = 2023
age=2026-year
try:
    if age>18:
        print("Eligible to vote")
    else:
        raise doException("Age is less than 18, not eligible to vote")
except doException:
    print("Caught an exception: Age is less than 18, not eligible to vote")

