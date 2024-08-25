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

row1 = ['x', ' ', 'o','o','o','o']
row2 = ['o', ' ', ' ',' ',' ',' ']
row3 = [' ', 'x', 'o','o','o','o']
row4 = [' ', 'x', 'o','o','o','o']
row5 = [' ', 'x', 'o','o','o','o']
row6 = [' ', 'x', 'o','o','o','o']

show_board([row1, row2, row3,row4,row5,row6])