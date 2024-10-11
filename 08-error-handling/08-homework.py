# intercept an error in except block
try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print('Can not do that, wrong types')
except:
    print('Oops, something went wrong')

print()
print()
print()

# intercept an error and do something in finally block
try:
    x = 5
    y = 0
    z = x / y
except:
    print('Not the way it is supposed to be')
finally:
    print('...but here we are')


print()
print()
print()

# write a function that asks for a number and prints its square using while and try-except
while True:
    try:
        num = input('Please pick a number: ')
        result = int(num) ** 2
        print(f'Here you go, squared: {result}')
    except:
        print('It is not a number, man...')
        continue
    else:
        break