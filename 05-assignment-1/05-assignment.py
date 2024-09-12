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

# Input with additional functionality to show help and log
def custom_input(st, log):
    result = None

    while not result:
        inp = input(st)

        if inp.lower() in ['help', 'h']:
            help_board = [[1,2,3],[4,5,6],[7,8,9]]
            print()
            print('The game features two players placing their signs on the available (empty) cells of the board, until one side\'s sign form a line or there is no available cells left.')
            print('Players get to act in turns, placing their signs on the board.')
            print('To choose what cell to put your sign in, use this map - number depicts a cell on the board.')
            show_board(help_board)
            print()
            continue
        elif inp.lower() == 'log':
            print(log['show']())
            print()
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

# Get user's chosen cell inndex 
def get_action_cell(board, log):
    cells = []

    for row in board:
        cells.extend(row)
    
    available_cells = [ind + 1 for ind, el in enumerate(cells) if not bool(str(el).strip())]
    chosen_cell_index = None

    while type(chosen_cell_index) != int:
        choice = custom_input('Choose a cell to make a move: ', log)

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

# Create a player object
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

# Create a log object with ability to write and read log entries
def start_log(data={ 'user': None, 'cell_index': None }):
    user = data['user']
    cell_index = data['cell_index']
    history = []

    def show_log():
        print()
        print('--------- Log Start ---------')
        for rec in history:
            userName = str(rec['user']['name']).capitalize()
            userSide = str(rec['user']['side']).upper()
            print(f'{userName} placed {userSide} to cell #{rec['move']}')
        print('--------- Log End ---------')

    log = {
        'history': history,
        'write': lambda user, cell_index: history.append({ 'user': user, 'move': cell_index + 1 }),
        'show': show_log
    }

    if user and int.is_integer(cell_index):
        log['write'](user, cell_index)

    return log 

# Ask user to make a move on a board (choose a cell to put X or O)
def make_a_move(player,board, log):
    print(f'{player['name'].capitalize()}, put a {player['side'].upper()} on a board...')

    action_cell_index = get_action_cell(board, log)
    row_index = floor(action_cell_index / 3)
    cell_index = action_cell_index % 3

    board[row_index][cell_index] = player['side']

    print()
    show_board(board)
    print()
    return action_cell_index

# Get board's cells as a flat list
def get_cells(board):
    cells = board[0].copy()
    cells.extend(board[1])
    cells.extend(board[2])
    return cells

# Check the board against winning combinations list
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

# Check for available cells on a board
def board_is_full(board):
    return get_cells(board).count(' ') == 0

# Perform a turn: both users making their moves
def make_turn(board, players, log = None):
    cells = get_cells(board)
    free_cells = cells.count(' ')

    if not bool(free_cells):
        print('No free cells left...')
        return None

    turns_done = (len(cells) - free_cells) / 2

    print(f'Turn #{turns_done + 1} begins...')

    winner = None

    for player in players:
        cell_index = make_a_move(player, board, log)

        if log:
            log['write'](player, cell_index)

        winner = check_winner(board, players)

        if winner:
            print(f'{player['name']} won, congratulations!!!!')
            break

    return winner

# Ask if userr wants to play again
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

# The game
def ttt(retry=False):
    log = start_log()

    if not retry:
        print('Hello and welcome to the TTT game!')

    print('Who\'s playing, lets register first player...')
    players = []
    sides = ['x', 'o']

    players.append(add_player())
    sides.remove(players[0]['side'])
    print()
    
    print('Okay, and the second player...')
    players.append(add_player(sides.pop()))
    print()

    board = get_board(3)
    print('Here is your playing board:')
    show_board(board)
    print()

    print('Lets start...')

    no_space_left = False
    winner = None

    while not winner and not no_space_left:
        winner = make_turn(board, players,log)
        no_space_left = board_is_full(board)

    again = try_again()
    if again:
        return ttt(True)
    else:
        print('Thanks for playing! Bye!')
        return
    
ttt()