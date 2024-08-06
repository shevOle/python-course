for num in range(5):
    print(num)
print()

for num in range(2,5):
    print(num)
print()

for num in range(1,5,2):
    print(num)
print()

# range is a generator, no value returned
print(range(5))
print(list(range(5)))
print('-----------------------------------')

word = 'askjfh'
for char in word:
    print(char)
print()

print(enumerate(word))
print(list(enumerate(word)))
print()

for smth in enumerate(word):
    print(smth)
print()

for i,char in enumerate(word):
    print(f'character {char} ar index position of {i}')
print('-----------------------------------')

list1 = [1,2,3]
list2 = ['a','b', 'c']
list3 = [21,45,73,56,778,3212]

print(zip(list1, list2))
print(list(zip(list1, list2)))
print()

list1.append(4)
list1.append(5)
# zips up to the length of the shortest list
print(list(zip(list1, list2)))
print(list(zip(list1, list2, list3)))
print()

for smth in zip((1,2,32), [5,6,7]):
    print(smth)
print()

for smth in zip(set([1,3,2,1,23,2,32]), [5,6,7,8,9,1,2]):
    print(smth)
print()

# dictionary is iterating through its keys
for smth in zip({'a':1, 'b':2,'c':3}, [5,6,7,8,9,1,2]):
    print(smth)
print()

# dictionaries are unordered, any key may be zipped here
for smth in zip({'a':1, 'b':2,'c':3,'c9':3,'c8':3,'c7':3,'c6':3,'c5':3,'c4':3,'c3':3,'c2':3,'c1':3}, [5,6,1,2,3,4,45,5]):
    print(smth)
print('-----------------------------------')

print('a' in 'ksdjgbjkakja')
# print(1 in 'ksdjhgkd')
print('1' in 'ksdjhgkd')
print(1 in range(3))
print(7 in range(3))
print()

dict1 = {'someKey': 'value1', 'key2': 124}
print('someKey' in dict1)
print('key45' in dict1)
print('value1' in dict1.values())
print('-----------------------------------')

my_range = list(range(3, 25))
print(min(my_range))
print(max(my_range))
print()

my_range.append(48)
print(max(my_range))
print('-----------------------------------')

result = input('Type a number: ')
print(result)
print(type(result))
print(float(result))
print(type(float(result)))