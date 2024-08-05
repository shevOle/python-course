a = 0
while a < 4:
    print(f'a is lees than 4 and equals to {a}')
    a += 1
print()

a = 5
while a < 4:
    print('will never get here')
else:
    print('entered else block immediately')
print()

a = 0
while a < 4:
    print(f'a is lees than 4 and equals {a}')
    a +=1
else:
    print('entering else block after looping')
print()