my_list = [1,2,3,4,5]

print(my_list[2])
print(my_list[2:])

another_list = ['six', 'seven']
concat_list = my_list + another_list
print(concat_list)

print(len(concat_list))
print(concat_list.count('six'))

concat_list.append('eigth')
print(len(concat_list))

popped_value = concat_list.pop()
print(popped_value)
print(concat_list)

another_popped = concat_list.pop(3)
print(another_popped)
print(concat_list)

num_list = [1,3,5,2,4,6,0]
sorted = num_list.sort()
print(sorted)
print(type(sorted))
print(num_list)

copy_list = num_list.copy()
print('list', num_list)
print('copy', copy_list)
print(num_list == num_list)
print(copy_list == num_list)
print(num_list == [1,2,3])

unsorted = [2,'r',67,1,'a',5,'s']
# unsorted.sort()
unsorted.reverse()
print(unsorted)

another_unsorted = [1,2.53,2.1,6,4.2,3]
another_unsorted.sort()
print(another_unsorted)