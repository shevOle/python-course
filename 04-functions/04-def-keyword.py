def print_hint(name, value):
    """
    Prints value with name formatted
    """
    print(name, ' -> ', value)
    print()

def print_hello(name):
    """
    Prints greeting to the person
    """
    print("Hello, " + name + "!")

print_hello('Oleh')
print()

def add_squares(num1, num2):
    """
    Adds squares of two numbers
    """
    print(num1**2 + num2**2)
add_squares(5, 22)
print()

def normalize_name(name):
    """
    Return name in lowercase
    """
    print(str(name).lower())
normalize_name('Some Name With Uppercase')
print()

# will fail with error, required argument
# normalize_name()

def normalize_name_with_default(name='Default'):
    """
    Return name in lowercase
    """
    print(str(name).lower())
normalize_name_with_default()
print()

# nothing returned from a function, re1 is None
res1 = add_squares(4,21)
print_hint('res1', res1)

def add_squares_with_return(num1, num2):
    """
    Adds squares of two numbers
    """
    return num1**2 + num2**2

# actualy returns a value that can be assigned to a variable
res2 = add_squares_with_return(4,21)
print_hint('res2', res2)