my_list = [1,2,3]

def show_list():
    print(my_list)

def choose_index():
    print()
    index = None

    while not index:
        show_list()
        choice = input('Choose and index to replace: ')

        if not choice.isdigit() or int(choice) not in range(1, len(my_list) + 1):
            print(f'Please, provide a valid index, number from 1 to {len(my_list)}')
            continue
        else:
            index = int(choice)
    
    return index

def choose_replacement():
    print()
    value = None

    while not value:
        choice = input('Provide a relacement for the value in the list: ')

        if len(choice) == 0:
            print('You have to provide a value')
            continue
        elif len(choice) > 10:
            print('Provided value is too long, 10 chars max')
            continue
        else:
            value = choice

    return value

def try_again():
    print()
    answers = {
        'y': True,
        'n': False
    }
    answer = None

    while type(answer) != bool:
        choice = input('Do you want to play more (y/n): ').lower()

        if choice not in answers:
            print("Please, provide 'y' or 'n' only")
            continue
        else:
            answer = answers[choice]
    
    return answer

def game(retry=False):
    if not retry:
        print('Hello in my game! Interact with console and change values in the list')

    index_to_update = choose_index()
    replacement_value = choose_replacement()
    my_list[index_to_update - 1] = replacement_value

    print('Here\'s the updated list, hooray!')
    show_list()
    print()

    again = try_again()

    if again:
        print()
        return game(True)
    else:
        return print('It was nice playing with you. Have a nice day!')
    
game()