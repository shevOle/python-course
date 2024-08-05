for char in 'some string of text':
    print(char)
print()

for num in [0,1,2]:
    print(f'the num is: {num}')
print()

num_sum = 0
for num in [0,1,2]:
    num_sum = num_sum + num
print(f'print without indent, out of the loop: {num_sum}')
print()

another_num_sum = 0
for num in [0,1,2]:
    another_num_sum = another_num_sum + num
    
    print(f'print with indent, inside the loop: {another_num_sum}')
print()
 
my_list = [3,4,5,6]
for num in my_list:
    print(f'from my_list: {num}')
print()
 
for num in my_list:
    if num % 2 == 0:
        print(f'even number: {num}')
    else:
        print(f'odd number: {num}')
print()
 
my_tuple = (1,3,5,6)
for num in my_tuple:
    print(f'from the tuple: {num}')
print()
 
my_dictionary = {"a":1, "b": 2, "c": 3}
for key in my_dictionary:
    print(f'from dictionary, key: {key}')
print()
 
for val in my_dictionary.values():
    print(f'from dictionary, value: {val}')
print()
 
my_set = set([1,2,4,5,5,2,1,6,3,2])
for num in my_set:
    print(f'from the set: {num}')
print()

# tuple unpacking
for (a,b) in [(1,2), (5,6), (9,5)]:
    print(f'first item of tuple: {a}')
    print(f'second item of tuple: {b}')
print()

# the same unpacking for list
for [a,b,c] in [[0,1,2], ['I will appear', 'I will not', 'I\'m too scared']]:
    print(f'first item in the list is: {a}')
print()

# using tuple unpacking with dictionary
for key, val in my_dictionary.items():
    print(f'from dictionary, key: {key}')
    print(f'from dictionary, val: {val}')
print()