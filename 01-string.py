print('hello\nworld')
print("I'm good, thanks")

print(len('what a damn long string you have here'))
print(len("I'm a string"))

my_string = 'some default string'

print(my_string[0])
print(my_string[-1])
print(my_string[-1] == my_string[len(my_string) - 1])

print(my_string[:4])
print(my_string[4:])
print(my_string[2:5])
print(my_string[::4])
print(my_string[::-1])

print(2+3)
print('2'+'3')

print(my_string.capitalize)
print(my_string.upper())
print(my_string.title())
print(my_string.capitalize())
print(my_string.split())

print('template: {}'.format('INERTED VALUE'))
print('template with 2 values: {} {}'.format('VALUE 1', 'VALUE 2'))
print('template with 2 the same values: {0} {0}'.format('VALUE 1', 'VALUE 2'))

value1 = 'VALUE 1'
value2 = 'VALUE 2'
print('template with values as variables: {value1} {value2}')
print('template with values as variables: {v1} {v2}'.format(v1='value 1', v2='value 2'))
print('template with values as variables: {1} {0}'.format(value2, value1))

# {value:width.precision f}
print('width.precision in action: {0:1.4f}'.format(1.245524362345))
print('width.precision in action: {:1.4f}'.format(1.245524362345))
print('width.precision in action: {0:10.4f}'.format(1.245524362345))
print('width.precision in action: {0:1.4f}'.format(12342.245524362345))

print('like a table')
print('{:3} | {:10}'.format('No.', 'Name'))
print('{:3} | {:10}'.format(1, 'Alexa'))
print('{:3} | {:10}'.format(2, 'George'))
print('{:3} | {:10}'.format(3, 'Michael'))

print('table with alignment')
print('{:3} | {:10}'.format('No.', 'Name'))
print('{:^3} | {:^10}'.format(1, 'Alexa'))
print('{:>3} | {:>10}'.format(2, 'George'))
print('{:<3} | {:<10}'.format(3, 'Michael'))

print('alignment spaces filled with char')
print('{:-<3} | {:.>10}'.format('No.', 'Name'))
print('{:=^3} | {:s^10}'.format(1, 'Alexa'))

print(f'the new string interpolation: {value1}')
print(f'the new string interpolation: {1.21421432:1.2f}')

print('some string with inserted value of %s' %'this')
print('some string with inserted value of %r' %'this')
print(f'some string with inserted value of {'this'!r}')
print('some string with inserted number as string %s' %43.2)
print('some string with inserted number as int %d' %43.2)
print(f'some string with inserted number as int {+43.2}')
print('precision example: %3.5f' %12.1532476344)
print("multiple values: %s %s %s %s" %(1,2,34,5))
print('multiple formatting: %d %4.2f %r %s' %(1.23, 1.2153, 'with quotes', 'without quotes'))