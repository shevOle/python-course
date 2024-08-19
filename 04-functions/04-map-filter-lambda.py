def square(num):
    return num ** 2

nums = [1,2,3,4,5,6]

result = map(square, nums)
print('just a result of map -> ', result)
print('making a list of map -> ', list(result))

# result itself is not an iterable, just a pointer 
for num in result:
    # never prinnting that
    print('result of map in for loop as a reference -> ', num)
print()
for num in map(square, nums):
    print('result of map in for loop -> ', num)

print('-----------------------------------------')

def is_even(num):
    return num % 2 == 0

result2 = filter(is_even, nums)
print('just a result of filter -> ', result2)
print('making a list of filter -> ', list(result2))

# result itself is not an iterable, just a pointer 
for num in result2:
    # never prinnting that
    print('result2 of filter in for loop as a reference -> ', num)
print()
for num in filter(is_even, nums):
    print('result2 of filter in for loop -> ', num)

print('-----------------------------------------')

square2 = lambda num: num ** 2
result3 = map(square2, nums)
print('result 3 using lambda func -> ', list(result3))
print()

result4 = map(lambda num: num ** 3, nums)
print('result4 using lambda inplace -> ', list(result4))
print()

result5 = filter(lambda num: num % 3 == 1, nums)
print('result5 using lambda inplace -> ', list(result5))
print()

result6 = [num ** 2 for num in filter(lambda num: num % 2 == 0, nums)]
print('result 6 for lambda inplace -> ', result6)