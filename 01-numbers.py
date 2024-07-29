int_number = 23
float_number = 43.32

# math order: power -> multiply, divide -> reminder -> add, substract
# 1. ... 2 ** 3 ...
# 2. 2 * ...
# 3. ... % 5 ...
# 4. ... - 5
print('2 * 2 ** 3 % 5 - 0.5 == 0.5 ----->', (2 * 2 ** 3 % 5 - 0.5) == 0.5)

print('int type', type(int_number))
print('float type', type(float_number))

print('int * float type', type(int_number * float_number))
print('float * float type', type(float_number * float_number))
print('int - int type', type(int_number - int_number))

print('float - float', float_number - float_number)
print('int - int', int_number - int_number)

print('floats comparison', int_number / float_number == int_number / float_number)