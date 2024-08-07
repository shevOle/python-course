s = 'Print only the words that starts with s in this sentence'
list1 = [f'{x}' for x in s.split() if x.lower()[0] == 's']
print(list1)
print()

list2 = [x for x in range(11) if x%2 == 0]
print(list2)
print()

list3 = [x for x in range(51) if x%3 == 0]
print(list3)
print()

s2 = 'Print every word in this sentence that has a even number of letters'
for i,x in enumerate(s2.split()):
    x_len = len(x)
    if x_len%2 == 0:
        print(f'{x} length is even and equals {x_len}')
print()

list4 = []
for x in range(1,101):
    s3 = ''
    if x%3 == 0:
        s3 += 'Fizz'
    if x%5 == 0:
        s3 += 'Buzz'
    list4.append(s3 or x)
print(list4)
print()

list5 = []
for x in range(1,101):
    s4 = f'{x%3 == 0 or '' and 'Fizz'}{x%5 == 0 or '' and 'Buzz'}'
    list5.append(s4 or x)
print(list5)
print()

s5 = 'Create a list of the first letters in every word of this string'
list6 = [x[0] for x in s5.split()]
print(list6)