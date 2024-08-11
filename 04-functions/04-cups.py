from random import shuffle

def set_difficulty():
    difficulty = int(input('Choose a difficulty from 3 to 10: '))
    
    if difficulty > 10 or difficulty < 3:
        print('Difficulty should be a number in a range from 3 to 10')
        print()
        set_difficulty()

    return difficulty

def try_again():
    answer = input('Want to try again (y/n)?')

    if answer.lower() == 'y':
        return True
    elif answer.lower() == 'n':
        return False
    else:
        print('Sorry, I did not understand you...')
        try_again()

def cups_game(repeat=False, difficulty = None):
    if not repeat:
        print('Hey! Welcome to the Cups Game!')
        
    if not difficulty:
        difficulty = set_difficulty()

    print('Shuffle shuffle...')
    cups_list = ([0] * (difficulty - 1))
    cups_list.append(1)
    shuffle(cups_list)
    ball_index = cups_list.index(1)

    guess = int(input(f'Under what cup is the ball, from 1 to {difficulty}: ')) - 1

    if guess == ball_index:
        print('You won!!!')
    else:
        print(f'No... The ball was under {ball_index + 1} cup')

    want_try_again = try_again()
    if want_try_again:
        cups_game(True, difficulty)
    else:
        print('It was nice seeing you, bye!')
        print()
        return
        
cups_game()