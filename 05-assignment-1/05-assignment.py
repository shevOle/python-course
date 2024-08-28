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

# row1 = ['x', ' ', 'o','o','o','o']
# row2 = ['o', ' ', ' ',' ',' ',' ']
# row3 = [' ', 'x', 'o','o','o','o']
# row4 = [' ', 'x', 'o','o','o','o']
# row5 = [' ', 'x', 'o','o','o','o']
# row6 = [' ', 'x', 'o','o','o','o']

# show_board([row1, row2, row3,row4,row5,row6])

# Prepare playing board
def get_board(cell_number=3):
    row = [' '] * cell_number
    board = [row] * cell_number
    return board  
  
# board1 = get_board(9)
# show_board(board1)

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

row1 = [' ', 'x', ' ']
row2 = ['o', 'x', ' ']
row3 = [' ', 'x', 'o']
board1 = [row1, row2, row3]

show_board(board1)
print(get_action_cell(board1))