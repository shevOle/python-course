def func1(*args):
    print('this is args -> ', args)
    print(type(args))
    print()

func1(1,2,3,4,5)
func1('a', 23, (3,6,8), { 'fruit': 'banana' })

def func2(**kwargs):
    print('this is kwargs ->', kwargs)
    print(type(kwargs))
    print()

# errors, need to pass key words
# func2(1,2,3)

func2(a=1, b=2, c=3)
func2(a=(1,2,3), b={ 'fruit': 'kiwi' })

print('---------------------------')

# still args, can be named differently
def func3(*aaa):
    print(aaa)

func3(1,2,3,4,5)

# still kwargs, can be named differently
def func4(**bbb):
    print(bbb)

func4(a=1, b=2, c=3)

print('---------------------------')

def sum_nums(num1, num2, *args):
    to_sum = [num1, num2]

    print('args in sum_nums -> ', args)
    for num in args:
        to_sum.append(num)

    print('number to sum -> ', to_sum)
    print('sum -> ', sum(tuple(to_sum)))

sum_nums(4,5)
sum_nums(4,5,4)
sum_nums(4,5,6,9,10,3,24,6,8,3)
# errored, expects at least 2 args
# sum_nums(4)

print('---------------------------')

def countdown(**kwargs):
    print('kwargs -> ', kwargs)
    stop_on = 5

    if 'stop' in kwargs:
        stop_on = kwargs['stop']

    index = 0

    while index < stop_on:
        print('counting: ', index)
        index += 1
    else:
        print('stoped on: ', index)
    print()

countdown()
countdown(fruit=2)
countdown(stor=3, start=6)
countdown(stop=2, finish=4)
countdown(stop=12)

print('---------------------------')

def func5(*args, **kwargs):
    print(args)
    print(kwargs)
    
func5(1,2,3,sun='no', moon='yeap')

# wrong syntax, arguments should be in order, no mixing
# func5(1,2, sun='no', 23,5, moon='yes')

# wrong syntax, can use only one * and one ** argument
# def func6(*args, **kwargs, *args2):
# def func7(*args, **kwargs, **kwargs2):