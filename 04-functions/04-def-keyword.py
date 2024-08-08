def print_hello(name):
    """
    Prints greeting to the person
    """
    print("Hello, " + name + "!")

print_hello('Oleh')

def add_squares(num1, num2):
    """
    Adds squares of two numbers
    """
    print(num1**2 + num2**2)
add_squares(5, 22)

def normalize_name(name):
    """
    Return name in lowercase
    """
    print(str(name).lower())
normalize_name('Some Name With Uppercase')