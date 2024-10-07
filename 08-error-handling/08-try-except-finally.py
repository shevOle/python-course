def adder(num1, num2):
    return num1 + num2

# went well
print(adder(1,6))
print('successful addition')
print()

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

print()

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