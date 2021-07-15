import random
import os
from constants import *


def clear_terminal():
    os.system("clear")


# This function accepts a list of variables, checks if any of these variables is not an integer and returns "False"
# else returns "True".
def validate_integers(integers):
    for integer in integers:
        if not isinstance(integer, int):
            return False
    
    return True


# This function accepts some parameters to create a board with the specified dimensions and number of mines.
# Raises a ValueError if any of the numbers provided is not an integer.
# Raises a ValueError if the number of mines provided exceeds the number of positions in the board.
def create_board(number_of_rows, number_of_columns, number_of_mines):
    if not validate_integers([number_of_rows, number_of_columns, number_of_mines]):
        raise ValueError("All the parameters provided should be integers")

    if number_of_mines > (number_of_rows * number_of_columns):
       raise ValueError("Number of mines cannot be larger than the number of cells in the board")

    # create an empty board with the specified dimensions
    board = []
    for row in range(number_of_rows):
        row_list = []
        for column in range(number_of_columns):
            row_list.append(" ")
        board.append(row_list)
    
    # populate the board with the specified number of mines
    counter = 0
    while counter < number_of_mines:
        row_index = random.randint(0, number_of_rows-1)
        column_index = random.randint(0, number_of_columns-1)
        if board[row_index][column_index] == "*":
            continue
        board[row_index][column_index] = "*"
        counter += 1
    
    return board


# This function accepts a board as a parameter and returns an integer representing the number of rows.
# Raises a ValueError if "board" is not a "list".
def get_number_of_rows(board):
    if not isinstance(board, list):
        raise ValueError("The provided board must be of type 'list'")

    return len(board)


# This function accepts a board as a parameter and returns an integer representing the number of columns.
# Raises a ValueError if "board" is not a "list".
# Raises a ValueError if "board" doesn't have equally long rows.
def get_number_of_columns(board):
    if get_number_of_rows(board) == 0:
        return 0
    
    number_of_columns = len(board[0])
    for row in board:
        if number_of_columns != len(row):
            raise ValueError("The provided board doesn't have equally long rows")

    return number_of_columns


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
# Raises a ValueError if "board" doesn't have equally long rows.
# Raises a ValueError if "row_index" is not an integer.
def is_column_index_in_range(board, column_index):
    if not validate_integers([column_index]):
        raise ValueError("The provided column index must be an integer")

    if column_index < 0 or column_index > (get_number_of_columns(board) - 1):
        return False
    
    return True


# This function takes a board and indices as parameters and returns the cell value specified by the indices.
# Raises a ValueError if "board" is not a "list".
# Raises a ValueError if "board" doesn't have equally long rows.
# Raises a ValueError if any of the indices provided is not an integer.
# Raises a ValueError if any of the indices provided is not in range of the board.
def get_cell_value(board, row_index, column_index):
    if not (is_row_index_in_range(board, row_index) and is_column_index_in_range(board, column_index)):
        raise ValueError("The indices provided should be in range of the board")

    return board[row_index][column_index]


# This function takes a board, 2 indices and a value as parameters and sets the value in the specified cell.
# Raises a ValueError if "board" is not a "list".
# Raises a ValueError if "board" doesn't have equally long rows.
# Raises a ValueError if any of the indices provided is not an integer.
# Raises a ValueError if any of the indices provided is not in range of the board.
# Raises a ValueError if the provided value is not an accepted value.
def set_cell_value(board, row_index, column_index, value):
    if not (is_row_index_in_range(board, row_index) and is_column_index_in_range(board, column_index)):
        raise ValueError("The indices provided should be in range of the board")
    
    if value not in ACCEPTED_CELL_VALUES:
        raise ValueError("The value provided is not an accepted value")

    board[row_index][column_index] = value


# This function asks the user for a choice, validates it and returns mixed types for response.
# Raises a ValueError if "board" is not a "list".
# Raises a ValueError if "board" doesn't have equally long rows.
# Raises a ValueError if the user inputs an unacceptable instruction.
# Returns a tuple if the instruction is acceptable, and its not "exit". The tuple is of the form (row, column, operation)
# Returns "None" if the user wants to exit.
def get_user_choice(board):
    # ask the user for a cell coordinates
    try:
        choice = input("What is your instruction? ")
    except KeyboardInterrupt:
        return None

    if choice == "exit":
        return None

    # we need to make sure the choice includes acceptable instructions
    operation = "reveal"

    try:
        if len(choice) > 3: # The user probably wants to flag or unflag a cell
            if choice[0:4] != "flag":
                raise ValueError("Wrong coordinates")
        
            operation = "flag"
            choice = choice[5:]

        try:
            row_index = CHARACTERS.index(choice[0])
        except ValueError: # This exception is thrown by the index() method
            raise ValueError("Wrong row coordinates")

        try:
            column_index = int(choice[1:])
        except ValueError: # This exception is thrown by the int() method
            raise ValueError("Wrong column coordinates")

    except IndexError: # This exception is thrown when we are trying to access a wrong index in "choice"
        raise ValueError("Wrong coordinates")

    if not is_row_index_in_range(board, row_index):
            raise ValueError("Wrong row coordinates")
    
    if not is_column_index_in_range(board, column_index):
        raise ValueError("Wrong column coordinates")

    return (row_index, column_index, operation)


# This function processes the chosen cell and updates the cell's value to show the number of surrounding mines.
# If the chosen cell contains a mine, this function returns "False". Otherwise it returns "True".
# If there are no surrounding mines, this function calls itself for each of the surrounding cells recursively.
# Raises a ValueError if "board" is not a "list".
# Raises a ValueError if "board" doesn't have equally long rows.
# Raises a ValueError if any of the indices provided is not an integer.
# Raises a ValueError if any of the indices provided is not in range of the board.
# Raises a ValueError if a wrong value is provided to set_cell_value().
def reveal_cell(board, row_index, column_index):
    cell_value = get_cell_value(board, row_index, column_index)

    # if user chooses a cell with a mine inside, the game is lost.
    if cell_value == "*":
        return False
    
    # skip if cell was already processed or flagged
    if cell_value != " ":
        return True

    # list representing the offsets to be added to the given indices inorder to obtain the indices for surrounding cells
    neighbour_indices = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # user didn't lose, calculate the number of surrounding mines
    number_of_mines = 0
    for neighbour_index in neighbour_indices:
        try:
            neighbour_row_index = row_index + neighbour_index[0]
            neighbour_column_index = column_index + neighbour_index[1]
            neighbour_cell_value = get_cell_value(board, neighbour_row_index, neighbour_column_index)

            if neighbour_cell_value == "*" or neighbour_cell_value == "#":
                number_of_mines += 1

        except ValueError:
            # This exception is thrown when the neighbour indices are out of board range
            continue
    
    set_cell_value(board, row_index, column_index, str(number_of_mines))

    # if there are no surrounding mines, open the surrounding cells recursively
    if number_of_mines == 0:
        for neighbour_index in neighbour_indices:
            try:
                neighbour_row_index = row_index + neighbour_index[0]
                neighbour_column_index = column_index + neighbour_index[1]
                reveal_cell(board, neighbour_row_index, neighbour_column_index)
            except ValueError:
                # This exception is thrown when the neighbour indices are out of board range
                continue

    return True

# This function accepts a board and indices as parameters and flags/unflags the specified cell.
# Raises a ValueError if "board" is not a "list".
# Raises a ValueError if "board" doesn't have equally long rows.
# Raises a ValueError if any of the indices provided is not an integer.
# Raises a ValueError if any of the indices provided is not in range of the board.
# Raises a ValueError if a wrong value is provided to set_cell_value().
def flag_cell(board, row_index, column_index):
    cell_value = get_cell_value(board, row_index, column_index)

    # flag or unflag the cell with the appropriate value from the FLAG_MAP
    set_cell_value(board, row_index, column_index, FLAG_MAP[cell_value])


# This function checks all the cells in the board and returns "False" if at least 1 cell is not processed yet.
# In other words, if any cell contains a space " " the function returns "False". Otherwise it returns "True".
def is_game_won(board):
    for row in board:
        for cell_value in row:
            if cell_value == " ":
                return False
    
    return True


# This function accepts a board and prints it to the terminal in a certain style with indices.
# If "show_mines" is passed as "True", print each cell as it is, except if the cell contains "#" we need to print it as "F".
# If "show_mines" is passed as "False", print each cell with the appropriate value from the PRINT_MAP.
# Raises a ValueError if "board" is not a "list".
# Raises a ValueError if "board" doesn't have equally long rows.
# Raises a ValueError if the number of rows in the board is greater than 16 (the number of characters available).
def print_board(board, show_mines = False):
    if get_number_of_rows(board) > len(CHARACTERS):
        raise ValueError(f"Number of rows in the board cannot be larger than {len(CHARACTERS)}")
    
    # generate the header and row-separator outputs
    header = "   "
    row_separator = "  "
    for index in range(get_number_of_columns(board)):
        header += " " + str(index) + " "
        if index < 10:
            header += " "
        row_separator += "  - "

    output_list = [header, row_separator]

    # generate the board output
    for row_index, row in enumerate(board):
        output = CHARACTERS[row_index] + " | "
        for cell_value in row:
            if show_mines: # print each cell as it is, except if the cell contains "#" we need to print it as "F"
                if cell_value == "#":
                    printed_value = "F"
                else:
                    printed_value = cell_value
            else: # print each cell with the appropriate value from the PRINT_MAP
                printed_value = PRINT_MAP[cell_value]

            output += printed_value + " | "
        output_list.append(output)
        output_list.append(row_separator)

    # print the output
    for output_row in output_list:
        print(output_row)

