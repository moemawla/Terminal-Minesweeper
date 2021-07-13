import random
from functions import *

def create_board(number_of_rows, number_of_columns, number_of_mines):
    # raise an exception if any of the numbers provided is not an integer
    validate_integers([number_of_rows, number_of_columns, number_of_mines], 'All the parameters provided should be integers')

    # raise an exception if the number of mines provided exceeds the number of positions in the board
    if number_of_mines > (number_of_rows * number_of_columns):
       raise ValueError('Number of mines cannot be larger than the number of cells in the board')

    # create an empty board with the specified dimensions
    board = []
    for row in range(number_of_rows):
        row_list = []
        for column in range(number_of_columns):
            row_list.append(' ')
        board.append(row_list)
    
    # populate the board with the specified number of mines
    counter = 0
    while counter < number_of_mines:
        row_index = random.randint(0, number_of_rows-1)
        column_index = random.randint(0, number_of_columns-1)
        if board[row_index][column_index] == '*':
            continue
        board[row_index][column_index] = '*'
        counter += 1
    
    return board

def print_board(board):
    characters = 'abcdefghijklmnop'

    # raise an exception if the number of rows in the board is greater than the number of characters available
    if len(board) > len(characters):
        raise ValueError(f'Number of rows in the board cannot be larger than {len(characters)}')
    
    # generate the header and row-separator outputs
    header = '   '
    row_separator = '  '
    for index in range(get_number_of_columns(board)):
        header += ' ' + str(index) + ' '
        if index < 10:
            header += ' '
        row_separator += '  - '

    output_list = [header, row_separator]

    # generate the board output
    for row_index, row in enumerate(board):
        output = characters[row_index] + ' | '
        for column_index, value in enumerate(row):
            printed_value = value
            # check if the cell contains a mine, print an empty space instead to hide the mine
            if value == '*':
                printed_value = ' '
            output += printed_value + ' | '
        output_list.append(output)
        output_list.append(row_separator)

    
    # print the output
    for row in output_list:
        print(row)




print_board(create_board(16, 10, 5))
