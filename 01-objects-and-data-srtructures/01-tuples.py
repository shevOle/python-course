t1 = (1,2,3)
l1 = [1,2,3]
print(t1 == l1)
print(type(t1))
print(len(t1))

l1[1] = 123
print(l1)

# t1[1] = 1234

t2 = (1,4,2,6,1,2,5,1)
print(t2.count(1))
print(t2.index(1))