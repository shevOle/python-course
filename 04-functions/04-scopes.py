# the order of variable search accross namespaces is
# 1. local namespace
# 2. enclosing scope's namespace
# 3. global namespace
# 4. Python namespace, reserved variables' names

# if a variable wasn't found in closest namespace, 
# the search continues inn the next one:
# if not found in LOCAL - look into ENCLOSING
# if not found in ENCLOSING - look into GLOBAL, etc.

# ----------------------------------------------------

# global level variable, global namespace
x = 3

def a():
    # local level variable, local namespace
    # will not reassign the global variable, but will create a local variable
    x = 5
    print(f'from local namespace: {x}')

# check variable reassigning
print(f'from global namespace: {x}')
a()
print(f'recheck global variable: {x}')
print()

def b():
    x = 10
    def c():
        # it will print a variable from the closest namespace
        # closest one is in enclosing function, because there is no local variable available
        print(f'Printing the X from an enclosing namespace: {x}')

    c()
b()
print()

def d():
    x = 15
    # will print an X from  the local namespace
    print(f'value of X: {x}')
    
    def e():
        # keyword to access a global variable from a namespace
        global x
        x = 25        

        print(f'reassigned the global variable X: {x}')

    e()
d()

# will be equal 25, because of "global" keyword used
print(f'recheck the global X: {x}')