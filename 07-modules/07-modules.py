from simple_module import simple_func
simple_func()

# from Packages import module as module0
from Packages.module import print__bool
print__bool()

# from Packages.Numbers import module as module1
from Packages.Numbers.module import print_number
print_number()

# from Packages.Strings import module as module2
from Packages.Strings.module import print_string
print_string()

# __name__ indicates how the module was run: directly or by being imported in other module and run from there
print(f'__name__ in modules file being run directly is {__name__}')

if __name__ == "__main__":
    print('run directly')
    # it is the common way to run scripts if module was run diirectly
    # if module was imported you do not run anything except methods being used in the file that imports it