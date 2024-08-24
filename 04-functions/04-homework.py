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

# Write a function that takes a list and returns a new list with unique elements of the first list
def unq_list(li):
    return list(set(li))

my_list = [1,1,2,3,4,1,2,4,2]
print(f'original list: {my_list}')
print(f'unique values: {unq_list(my_list)}')
print()

def unq_list2(li):
    known_elements = []
    for item in li:
        if item not in known_elements:
            known_elements.append(item)

    return known_elements

print(f'original list: {my_list}')
print(f'unique values: {unq_list2(my_list)}')
print()

print('---------------------------------------')

# Write a function to multiply all the numbers in a given list
def multiply_nums(li):
    result = 1
    for num in li:
        result *= num

    return result

print(f'list to multiply: {my_list}')
print(f'multiplication result: {multiply_nums(my_list)}')
print()

print('---------------------------------------')

# Write a function that checks whether a word or phrase is a palindrome or not
# Palindrom - is a string that reads forward and backward the same

def is_palindrome(st):
    normalized_str = ''.join([char for char in st if char.isalpha()]).lower()
    return normalized_str == normalized_str[::-1]

my_word = 'helleh'
my_word1 = 'hellehe'
pali_phrase = 'Cigar? Toss it in a can. It is so tragic.'
print(f'check if {my_word} is a palindrome: {is_palindrome(my_word)}')
print(f'check if {my_word1} is a palindrome: {is_palindrome(my_word1)}')
print(f'check if {pali_phrase} is a palindrome: {is_palindrome(pali_phrase)}')
print()

print('---------------------------------------')

# Write a function to check whether a string is pangram (contains every letter of alphabet) or not
pangram_string = 'The quick brown fox jumps over the lazy dog'
not_pangram = 'I\'m not a pangram'

from string import ascii_lowercase

def is_pangram(st):
    letters = set([char.lower() for char in st if str(char).isalpha()])
    return len(letters) == len(ascii_lowercase)

print(f'String "{pangram_string}" is pangram: {is_pangram(pangram_string)}')
print(f'String "{not_pangram}" is pangram: {is_pangram(not_pangram)}')
print()

def is_pangram2(st):
    letters = [char.lower() for char in st if str(char).isalpha()]
    sorted_letters = list(set(letters))
    sorted_letters.sort()

    return sorted_letters == list(ascii_lowercase)
    # OR
    # return ''.join(sorted_letters) == ascii_lowercase

print(f'String "{pangram_string}" is pangram: {is_pangram2(pangram_string)}')
print(f'String "{not_pangram}" is pangram: {is_pangram2(not_pangram)}')
print()

def is_pangram3(st):
    is_pangram_string = True    
    index = 0
    while is_pangram_string and index < len(ascii_lowercase):
        letter = ascii_lowercase[index]
        index += 1
        is_pangram_string = bool(str(st).count(letter))

    return is_pangram_string

print(f'String "{pangram_string}" is pangram: {is_pangram3(pangram_string)}')
print(f'String "{not_pangram}" is pangram: {is_pangram3(not_pangram)}')
print()