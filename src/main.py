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





b = create_board(10, 10, 5)
for row in b:
    print(row)
