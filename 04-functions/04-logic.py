def is_odd(number):
    return number % 2 == 0

print(is_odd(16))
print(is_odd(17))
print(is_odd(18))
print(is_odd(19))
print()

def list_some(arr, func):
    result = False
    index = 0

    while not result and index < len(arr):
        result = func(arr[index])
        index += 1
    
    return result

list1 = [1,3,5,7,9]
list2 = [1,3,5,8,9]

print('has even, list with odd only nums -> ', list_some(list1, is_odd))
print('has even, list with 1 even num -> ', list_some(list2, is_odd))
print()

def list_has_char(char):
    def char_in(str):
        return char in str
    
    return char_in

list3 = ['ssss', 'aaa', 'ikdjsf']
list4 = ['ssss', 'a', 'ikdjsf']
list5 = ['ssss', 'ldfkgj', 'ikdjsf']

print('has char "a", list with "aaa" el -> ', list_some(list3, list_has_char('a')))
print('has char "a", list with "a" el -> ', list_some(list4, list_has_char('a')))
print('has char "a", list without "a"s -> ', list_some(list5, list_has_char('a')))
print()

def list_check(arr, func, return_elements = False):
    fitting_elements = []

    for el in arr:
        if func(el):
            fitting_elements.append(el)

    result = len(fitting_elements) > 0

    if return_elements:
        return (result, fitting_elements)
    else:
        return result
    
check_list3 = list_check(list3, list_has_char('a'))
(check_list3_bool, check_list3_arr) = list_check(list3, list_has_char('a'), True)
check_list5 = list_check(list5, list_has_char('a'))
(check_list5_bool, check_list5_arr) = list_check(list5, list_has_char('a'), True)

print('without returned elements, has char "a", list with "aaa" el -> ', check_list3)
print('with returned elements, RESULT, has char "a", list with "aaa" el -> ', check_list3_bool)
print('with returned elements, ARR, has char "a", list with "aaa" el -> ', check_list3_arr)
print()
print('without returned elements, has char "a", list without "a"s -> ', check_list5)
print('with returned elements, RESULT, has char "a", list without "a"s -> ', check_list5_bool)
print('with returned elements, ARR, has char "a", list without "a"s -> ', check_list5_arr)
print()