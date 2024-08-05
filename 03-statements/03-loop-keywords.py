x = 0
while True:
    print(f'infinite loop, x is {x}')
    x += 1

    if x > 5:
        # break the closest loop immediately
        break
print()

x = 0
while x < 10:
    x += 1
    if x % 2 != 0:
        # do nothing in the current loop's iteration
        pass
    else:
        print(f'x is an even number - {x}')
    print('still in the loop')
print()

x = 0
while x < 10:
    x += 1
    if x % 2 != 0:
        # skip current loop iteration
        continue
    else:
        print(f'x is an even number - {x}')
    print(f'got here while x is even')
print()

for num in [1,2,3,4]:
    if num == 3:
        break
    print(f'num is {num}')
print()

for num in [1,2,3,4]:
    if num == 3:
        continue
    print(f'num is {num}')
print()

for num in [1,2,3,4]:
    if num == 3:
        continue
    print(f'num is {num}')
print()