# Define a function that takes in a string 
# and returns a matching string where every even letter is uppercase, 
# and every odd letter is lowercase.

def str_transform(ex_string):
    char_list = [char.upper() if ind % 2 == 0 else char.lower() for ind, char in enumerate(str(ex_string))]
    return ''.join(char_list)

print(str_transform('oooooooooooooooooooooo'))
print()

def str_transform2(ex_string):
    result = ''
    for index, char in enumerate(str(ex_string)):
        if index % 2 == 0:
            result = result + char.upper()
        else:
            result = result + char.lower()

    return result

print(str_transform2('lllllllllllllllllllllll'))
print()

def str_transform3(ex_string):
    result = list(str(ex_string).lower())
    for ind in range(0, len(result), 2):
        result[ind] = result[ind].upper()
    
    return ''.join(result)

print(str_transform3('mmmmmmmmmmmmmmmmmmmmmm'))
print()

print('-------------------------------------------')

# Define a function called myfunc that takes in an arbitrary number of arguments, 
# and returns a list containing only those arguments that are even.

def return_even(*args):
    return [num for num in args if num % 2 == 0]

print(return_even(1,2,3,4,5,6,7,8,9,1214,35,124))

print('----------------------------')

# Given a sentence return a sentence with the words reversed

def yoda(sentence):
    result = str(sentence).split(' ')
    result.reverse()
    return ' '.join(result)

print(yoda('I am Yoda'))

def yoda2(sentence):
    return ' '.join(str(sentence).split(' ')[::-1])

print(yoda2('I am Yoda'))

print('----------------------------')

# Given a number return True if it's in range of 10 from 100 or 200 and False otherwise

def is_close(num):
    diff = 200 - num
    if -10 <= diff <= 10 or 90 <= diff <= 110:
        return True
    else:
        return False
    
print('shoud be True', is_close(98))
print('shoud be True', is_close(101))
print('shoud be True', is_close(193))
print('shoud be True', is_close(208))
print('shoud be True', is_close(110))
print('shoud be True', is_close(190))
print('shoud be True', is_close(200))
print('shoud be False', is_close(211))
print('shoud be False', is_close(150))
print('shoud be False', is_close(70))
print()

def is_close2(num):
    if abs(100 - num) <= 10 or abs(200 - num) <= 10:
        return True
    else:
        return False
    
print('shoud be True', is_close2(98))
print('shoud be True', is_close2(101))
print('shoud be True', is_close2(193))
print('shoud be True', is_close2(208))
print('shoud be True', is_close2(110))
print('shoud be True', is_close2(190))
print('shoud be True', is_close2(200))
print('shoud be False', is_close2(211))
print('shoud be False', is_close2(150))
print('shoud be False', is_close2(70))

print('----------------------------')

# Given a string and a pattern return number of all occurences of the pattern in the string

def occurences(st, pattern):
    occurences_num = 0

    index = 0
    while index < len(st):
        try:
            index = str(st).index(pattern, index) + 1
            occurences_num += 1
        except:
            break

    return occurences_num

print(occurences('hahahaha', 'hah'))
print(occurences('hahahaha', 'haha'))
print(occurences('hahahaha', 'hahah'))
print(occurences('hahahaha', 'ah'))
print(occurences('hahahaha', 'h'))

print('----------------------------')

# Given a string return a string where for each single char of the original string there will be 3 chars

def tripple(st):
    return ''.join([char*3 for char in st])

print(tripple('test string'))

print('----------------------------')

# Given three integers between 1 and 11, if their sum is less than of equal to 21, return their sum.
# If their sum esceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'.

def some_of(target_list, check_func):
    return True in [check_func(item) for item in target_list]

def out_of_range_comparator(range_tuple):
    def is_out_of_range(num):
        return num < range_tuple[0] or num > range_tuple[1]

    return is_out_of_range

def is_equal_comparator(target):
    def is_equal(item):
        return item == target
    return is_equal

def blackjack(a,b,c):
    if some_of([a,b,c], out_of_range_comparator((1,11))):
        return print('Pass three numbers from 1 to 11')
    
    result = sum((a,b,c))
    if result > 21 and some_of([a,b,c], is_equal_comparator(11)):
        result -= 10

    if result > 21:
        return 'BUST'
    else:
        return result
    
print('safe -> ', blackjack(1,1,1))
print('bust -> ', blackjack(11,11,11))
print('safe -> ', blackjack(11,11,9))
print('bust -> ', blackjack(11,11,10))
print('safe -> ', blackjack(7,7,7))
print('bust -> ', blackjack(10,10,10))
print()

# Give an array, return sum of all the numbers in the array,
# except ignore sections of numbers starting with 6 and ending with 6.
# Return 0 for non numbers

def adder(num_list):
    skip = False
    result = 0

    index = 0
    while index < len(num_list):
        num = num_list[index]
        is_number = isinstance(num, int)
        index += 1

        if num == 6 and not skip:
            skip = True
            continue

        if num == 9 and skip:
            skip = False
            continue

        if skip:
            continue

        if not is_number:
            continue

        result += num
    
    return result

print('to be 4 -> ', adder([1,2,6,7,8,9,1]))
print('to be 4 -> ', adder([1,2,6,6,8,9,1]))
print('to be 11 -> ', adder([1,9,6,7,8,9,1]))
print('to be 21 -> ', adder([1,2,6,7,9,8,9,1]))
print('to be 5 -> ', adder([1,2,6,7,9,1,6,8,9,1]))
print()

# def get_index(li, el):
#     has_el = bool(li.count(el))
#     if has_el:
#         return li.index(el)
#     else:
#         return None

# def get_splice_6_9(li):
#     index_6 = get_index(li, 6)
#     index_9 = get_index(li, 9)
    
#     if not index_6:
#         return li
#     else:
#         return li[index_6:index_9]
    
# def adder2(num_list):
#     li = list(num_list)

#     spliceable = bool(get_index(li, 6))
#     print(spliceable)
#     while spliceable:
#         li = splice_6_9(li)
#         spliceable = bool(get_index(li, 6))

#     return sum(li)

# print([1,2,3][:None])
# print(''.join(str([1,2,3,4])))
# []
# print('to be 4 -> ', adder2([1,2,6,7,8,9,1]))
# print('to be 4 -> ', adder2([1,2,6,6,8,9,1]))
# print('to be 11 -> ', adder2([1,9,6,7,8,9,1]))
# print('to be 21 -> ', adder2([1,2,6,7,9,8,9,1]))
# print('to be 5 -> ', adder2([1,2,6,7,9,1,6,8,9,1]))