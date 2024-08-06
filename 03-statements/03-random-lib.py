from random import shuffle
from random import randint
from random import choice
from random import randbytes
from random import randrange

list1 = list(range(1,25))
print(list1)
print()

# inplace function, mutates the list
result1 = shuffle(list1)
print(result1)
print(type(result1))
print(list1)
print()

print(randint(20,75))
print(randint(20,75))
print(randint(20,75))
print(randint(20,75))
print(randint(20,75))
print(randint(20,75))
print()

tuple1 = (1,'s', { 'a': 1 }, [1,3,45,7])
print(choice(tuple1))
print(choice(tuple1))
print(choice(tuple1))
print(choice(tuple1))
print(choice(tuple1))
print()

print(choice(range(15)))
print(choice(range(15)))
print(choice(range(15)))
print()

print(randbytes(10))
print()

print(randrange(15))
print(randrange(8,15))
print(randrange(8,15,2))
