import random

characters = 'abcdefghijklmnop'

# This function accepts a list of variables, checks if any of these variables is not an integer and returns "False"
# else returns "True".
def validate_integers(integers):
    for integer in integers:
        if not isinstance(integer, int):
            return False
    
    return True

# This function accepts a board as a parameter and returns an integer representing the number of rows.
# Raises a ValueError if "board" is not a "list".
def get_number_of_rows(board):
    if not isinstance(board, list):
        raise ValueError("The provided board must be of type 'list'")

    return len(board)

# This function accepts a board as a parameter and returns an integer representing the number of columns.
# Raises a ValueError if "board" is not a "list".
def get_number_of_columns(board):
    if get_number_of_rows(board) == 0:
        return 0
    
    return len(board[0])

# This function accepts a board and a row index as parameters and checks if the index is in range of the board.
# Raises a ValueError if "board" is not a "list".
# Raises a ValueError if "row_index" is not an integer.
def is_row_index_in_range(board, row_index):
    if not validate_integers([row_index]):
        raise ValueError("The provided row index must be an integer")

    if row_index < 0 or (row_index > (get_number_of_rows(board) - 1)):
        return False
    
    return True

# This function accepts a board and a column index as parameters and checks if the index is in range of the board.
# Raises a ValueError if "board" is not a "list".
# Raises a ValueError if "row_index" is not an integer.
def is_column_index_in_range(board, column_index):
    if not validate_integers([column_index]):
        raise ValueError("The provided column index must be an integer")

    if column_index < 0 or column_index > (get_number_of_columns(board) - 1):
        return False
    
    return True

# This function accepts some parameters to create a board with the specified dimensions and number of mines.
# Raises a ValueError if any of the numbers provided is not an integer.
# Raises a ValueError if the number of mines provided exceeds the number of positions in the board.
def create_board(number_of_rows, number_of_columns, number_of_mines):
    if not validate_integers([number_of_rows, number_of_columns, number_of_mines]):
        raise ValueError('All the parameters provided should be integers')

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

# This function accepts a board and prints it to the terminal in a certain style with indices.
# Raises a ValueError if "board" is not a "list".
# Raises a ValueError if the number of rows in the board is greater than 16 (the number of characters available).
def print_board(board):
    if get_number_of_rows(board) > len(characters):
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
    for output_row in output_list:
        print(output_row)

# This function asks the user for a choice, validates it and returns mixed types for response.
# Raises a ValueError if "board" is not a "list".
# Raises a ValueError if the user inputs unacceptable choice.
# Returns "None" if the user wants to exit.
# Returns a tuple if the row and column indices are acceptable.
def get_user_choice(board):
    # ask the user for a cell coordinates
    try:
        choice = input('Which cell you want to open? ')
    except KeyboardInterrupt:
        return None

    if choice == 'exit':
        return None

    # we need to make sure the choice includes acceptable row and column indices
    if len(choice) < 2:
        raise ValueError('Wrong coordinates')

    try:
        row_index = characters.index(choice[0])
    except ValueError:
        raise ValueError('Wrong row coordinates')
    
    if not is_row_index_in_range(board, row_index):
        raise ValueError('Wrong row coordinates')

    try:
        column_index = int(choice[1:])
    except ValueError:
        raise ValueError('Wrong column coordinates')

    if not is_column_index_in_range(board, column_index):
        raise ValueError('Wrong column coordinates')

    return (row_index, column_index)
