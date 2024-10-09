def adder(num1, num2):
    return num1 + num2

# went well
print(adder(1,6))
print('successful addition')
print('-----------------------------------')

# will produce an error and break the script
# print(adder(34, 'yogurt'))
# print('never gets here')

try:
    # will throw an error
    result = adder(2, 'string')
    print('no chance')
except:
    # we get here because of an error
    print('here we are')

print('-----------------------------------')

try:
    # no error is thrown here
    result2 = adder(2,6)
    print('yeah, baby')
except:
    # so we won't get to this print statement
    print('did not get here')
else:
    # but we will get here eventually
    print('but got here instead')

print('-----------------------------------')

try:
    file = open('someFile', 'r')
    file.write('will not write')
# can catch different type of errors and assign specific code blocks
except TypeError:
    # will not get here, because error will not be of TypeError kind
    print('TypeError got caught')
except OSError:
    print('OS Error got caught')

print('-----------------------------------')

try:
    file = open('someFile', 'w')
    file.write({"a": 1})
# can catch different type of errors and assign specific code blocks
except TypeError:
    print('TypeError got caught')
except OSError:
    # will not get here, because error will not be of OSError kind
    print('OS Error got caught')

print('-----------------------------------')

try:
    file = open('someFile', 'w')
    file.write({"a": 1})
except TypeError:
    print('TypeError got caught')
except:
    print('Will I run or not?')
# can add finally block to execute something after error, for example clean up
finally:
    print('I will execute no matter what')