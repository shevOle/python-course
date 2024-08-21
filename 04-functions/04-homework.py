# Write a function that computes the volume of a sphere given its radius
from math import pi

def sphere_volume(radius):
    return 4 / 3 * pi * radius ** 3

print(f'volume of sphere with radius 2: {sphere_volume(2)}')
print(f'volume of sphere with radius 5: {sphere_volume(5)}')
print()

print('---------------------------------------')

# Write a function that checks whether a number is in given range (inclusive of high annd low)
def in_range(num, min_num, max_num):
    return num in range(min_num, max_num + 1)

print(f'check for 3 in 1-5 range: {in_range(3, 1, 5)}')
print(f'check for 5 in 1-5 range: {in_range(5, 1, 5)}')
print(f'check for 7 in 1-5 range: {in_range(7, 1, 5)}')
print()

print('---------------------------------------')

# Write a function that accepts a string  and calculates the number of uppercase and lowercase letters
def check_casing(char):
    if char.islower():
        return 1
    elif char.isupper():
        return 2
    else:
        return 0

def get_case_stat(st):
    stats = list(map(check_casing, list(st)))

    print(f'Original string: {st}')
    print(f'Original string length: {len(st)}')
    print()
    print(f'No. of upper case characters: {stats.count(2)}')
    print(f'No. of lower case characters: {stats.count(1)}')
    print(f'No. of neither upper or lower case characters: {stats.count(0)}')
    
get_case_stat('Hello, Mr. Rogers. How are you this fine Tuesday?')
print()

print('---------------------------------------')