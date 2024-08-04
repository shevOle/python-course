a1 = {'k1': 1, 'k2': 2}
print(a1)
print(a1['k1'])
print(a1.keys())
print(a1.values())

a2 = {'k1': 2, 'k2': [1,4,6], 'k3': {'n1': 4}}
print(a2['k2'])
print(a2['k2'][1])
print(a2['k3'])
print(a2['k3']['n1'])

duplicate_a1 = {'k1': 1, 'k2': 2}
copy_a1 = a1.copy()
print(duplicate_a1 == a1)
print(copy_a1 == a1)

duplicate_a2 = {'k1': 2, 'k2': [1,4,6], 'k3': {'n1': 4}}
copy_a2 = a2.copy()
print(duplicate_a2 == a2)
print(copy_a2 == a2)

copy_a2['k3']['n1'] = 18
print(copy_a2['k3']['n1'])
print(a2['k3']['n1'])

# a2.update(['k1', 421])
# print(a2)
# a2.update(['n1', 23])
# print(a2)
a3 = {'k12': 123332}
a2.update(a3)
print(a2)