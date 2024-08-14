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