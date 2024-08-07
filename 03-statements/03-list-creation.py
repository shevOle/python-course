word = 'ksjdgfdoasljf'
list1 = []
for letter in word:
    list1.append(letter)
print(list1)
print()

list2 = [letter for letter in word]
print(list2)
print()

list3 = [x for x in word]
print(list3)
print()

list4 = [x**2 for x in range(10)]
print(list4)
print()

list5 = [x for x in range(10) if x%2 == 0]
print(list5)
print()

list6 = [x**2 for x in range(10) if x%2 == 0]
print(list6)
print()

list7 = [x**2 if x%2 == 0 else 'None' for x in range(10)]
print(list7)
print()

list8 = []
for x in [1,2,3]:
    for y in [1, 10, 100]:
        list8.append(x*y)
print(list8)

list9 = [x*y for x in [1,2,3] for y in [1,10,100]]
print(list9)