my_set = set()
print(my_set)

my_set.add(1)
print(my_set)

my_set.add(1)
print('add two 1s',my_set)

my_dictionary = { 'a': 1, 'b': 3, 'c': { 'a': 2, 'b': 3 } }
my_tupple = (1,2,3,4)

# my_set.add(my_dictionary) - can not add dictionary to a set

my_set.add(my_tupple)
print('add tupple', my_set)

my_list = [3,1,2,4,6,3,4,5]
set_of_list = set(my_list)
print('set of list', set_of_list)

print('difference', set_of_list.difference(my_set))
print('symmetric difference', set_of_list.symmetric_difference(my_set))

float_set = set()
float_set.add(10 / 3)
float_set.add(10 / 3)
print('set of floats', float_set)

char_set = set("Mississippi")
print('mississippi  into set', char_set)