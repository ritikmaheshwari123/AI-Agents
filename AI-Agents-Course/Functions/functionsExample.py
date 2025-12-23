## Password strength checker function
def check_password_strength(password):  
    """Check the strength of a given password.

    Args:
        password (str): The password to check.

    Returns:
        str: A message indicating the strength of the password.
    """
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        return "Strong password"
    elif length >= 8 and (has_upper + has_lower + has_digit + has_special) >= 3:
        return "Moderate password"
    else:
        return "Weak password"

## check if string is palindrome
def is_palindrome(s):
    """Check if the given string is a palindrome.

    Args:
        s (str): The string to check.
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    s = s.lower().replace(" ", "").replace(",", "").replace(".", "")
    return s == s[::-1] 

## factorial of a number using recursion
def factorial(n):
    """Calculate the factorial of a number using recursion.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of the number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

## read a file and count frequency of each word
def word_frequency(file_path):
    """Read a file and count the frequency of each word.

    Args:
        file_path (str): The path to the file.      
    Returns:
        dict: A dictionary with words as keys and their frequencies as values.
    """
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?;"\'()[]{}')
                word_count[word] = word_count.get(word, 0) + 1
    return word_count

## Validate email address
def validate_email(email):
    """Validate the format of an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email format is valid, False otherwise.
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
    

# Example usage
password = "StrongP@ssw0rd!"
print(f"Password: {password} - {check_password_strength(password)}")
test_string = "A man, a plan, a canal: Panama"  
print(f"String: '{test_string}' - Is palindrome? {is_palindrome(test_string)}")
number = 5
print(f"Factorial of {number} is {factorial(number)}")
file_path = "samples.txt"  # Make sure to have a sample.txt file in the same directory
print(f"Word frequency in '{file_path}': {word_frequency(file_path)}")
email = "ritik.maheshwari@gmail.com"
print(f"Email: {email} - Valid format? {validate_email(email)}")

