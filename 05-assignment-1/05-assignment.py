from math import floor

# Show a row for any number of cells
def show_row(row):
    printed_row = ''
    for ind, item in enumerate(row):
        if ind < len(row) - 1:
            printed_row += f' {item} |'
        else:
            printed_row += f' {item} '
    print(printed_row)

# Show a board of Tik-Tak-Toe
def show_board(rows):
    for row in rows:
        show_row(row)

def show_help():
    print()

def input_with_help(st):
    result = None

    while not result:
        inp = input(st)

        if inp.lower() in ['help', 'h']:
            help_board = [[1,2,3],[4,5,6],[7,8,9]]
            print('The game features two players placing their signs on the available (empty) cells of the board, until one side\'s sign form a line or there is no available cells left.')
            print('Players get to act in turns, placing their signs on the board.')
            print('To choose what cell to put your sign in, use this map - number depicts a cell on the board.')
            show_board(help_board)
            continue
        else:
            result = inp

    return result

# Prepare playing board
def get_board(cell_number=3):
    row = [' '] * cell_number
    board = []

    for _ in range(0, cell_number):
        board.append(row.copy())

    return board  

def get_action_cell(board):
    cells = []

    for row in board:
        cells.extend(row)
    
    available_cells = [ind + 1 for ind, el in enumerate(cells) if not bool(str(el).strip())]
    chosen_cell_index = None

    while type(chosen_cell_index) != int:
        choice = input('Choose a cell to make a move: ')

        if not choice.isdigit():
            print('Please, provide a positive number')
            continue
        elif int(choice) not in range(1, len(cells) + 1):
            print(f'Choose a number between 1 and {len(cells)}')
            continue
        elif int(choice) not in available_cells:
            print(f'Cell {choice} was already picked, here\'s the board: ')
            show_board(board)
            continue
        else:
            chosen_cell_index = int(choice) - 1
    
    return chosen_cell_index

def add_player(chosen_side=None):
    player = {
        'name': None,
        'side': chosen_side,
    }
    
    while not player['name']:
        name = input('What is your name: ').strip()

        if len(name) == 0:
            print('Please provide a name')
            continue
        
        player['name'] = name

    while not player['side']:
        side = input('What side will you choose (X or O): ').strip().lower()

        if side not in ['x', 'o']:
            print('Please, choose either X or O')
            continue
        
        player['side'] = side

    return player    

def start_log(user, cell_index):
    history = []

    def show_log():
        for rec in history:
            print(f'{str(rec['user']['name']).capitalize()} placed {str(rec['user']['side']).upper()} to cell #{rec['move']}')

    log = {
        'history': history,
        'write': lambda user, cell_index: history.append({ 'user': user, 'move': cell_index + 1 }),
        'show': show_log
    }

    log['write'](user, cell_index)

    return log 

def make_a_move(player,board):
    print(f'{player['name'].capitalize()}, put a {player['side'].upper()} on a board...')

    action_cell_index = get_action_cell(board)
    row_index = floor(action_cell_index / 3)
    cell_index = action_cell_index % 3

    board[row_index][cell_index] = player['side']
    
    print()
    show_board(board)
    print()



def get_cells(board):
    cells = board[0].copy()
    cells.extend(board[1])
    cells.extend(board[2])
    return cells

def check_winner(board, players):
    cells = get_cells(board)

    winning_combinations = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,4,8],
        [2,4,6],
        [0,3,6],
        [1,4,7],
        [2,5,8]
    ]

    game_winner = None
    for combination in winning_combinations:
        state = [cells[ind].lower() for ind in combination]
        check = list(map(lambda player: state.count(player['side']) == 3, players))
        
        if True in check:
            game_winner = players[check.index(True)]
            break

    return game_winner

def board_is_full(board):
    return get_cells(board).count(' ') == 0

def make_turn(board, players):
    cells = get_cells(board)
    free_cells = cells.count(' ')

    if not bool(free_cells):
        print('No free cells left...')
        return None

    turns_done = (len(cells) - free_cells) / 2

    print(f'Turn #{turns_done + 1} begins...')

    winner = None

    for player in players:
        make_a_move(player, board)
        winner = check_winner(board, players)

        if winner:
            print(f'{player['name']} won, congratulations!!!!')
            break

    return winner
        
def try_again():
    response = None

    while not response:
        inp = input('Want to try again (y/n)?')

        if inp.lower() not in ['y', 'n']:
            print("Please, provide either 'y' or 'n'...")
            continue
        else:
            response = inp.lower()

    return response == 'y'


def ttt(retry=False):
    if not retry:
        print('Hello and welcome to the TTT game!')

    print('Who\'s playing, lets register first player...')
    players = []
    players.append(add_player())
    print()
    print('Okay, and the second player...')
    # TODO: set second side automatically
    players.append(add_player())
    print()

    board = get_board(3)
    print('Here is your playing board:')
    show_board(board)
    print()

    print('Lets start...')

    no_space_left = False
    winner = None

    while not winner and not no_space_left:
        winner = make_turn(board, players)
        no_space_left = board_is_full(board)

    again = try_again()
    if again:
        return ttt(True)
    else:
        print('Thanks for playing! Bye!')
        return
    
ttt()