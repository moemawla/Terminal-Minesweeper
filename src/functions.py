import random
import os
import json
from constants import *
from termcolor import colored


def clear_terminal():
    os.system("clear")

def print_banner():
    clear_terminal()
    print('''
████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗                              
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║                              
   ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║                              
   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║                              
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗                         
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝                         
███╗   ███╗██╗███╗   ██╗███████╗███████╗██╗    ██╗███████╗███████╗██████╗ ███████╗██████╗ 
████╗ ████║██║████╗  ██║██╔════╝██╔════╝██║    ██║██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗
██╔████╔██║██║██╔██╗ ██║█████╗  ███████╗██║ █╗ ██║█████╗  █████╗  ██████╔╝█████╗  ██████╔╝
██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ╚════██║██║███╗██║██╔══╝  ██╔══╝  ██╔═══╝ ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║██║ ╚████║███████╗███████║╚███╔███╔╝███████╗███████╗██║     ███████╗██║  ██║
╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
    ''', end="\n\n")


# This function accepts a list of variables, checks if any of these variables is not an integer and returns "False"
# else returns "True".
def validate_integers(integers):
    for integer in integers:
        if not isinstance(integer, int):
            return False
    
    return True

# This function aks the user for the game difficulty, and returns a string representing the chosen difficulty.
# If the user inputs an unacceptable choice, the function prints an error message and asks the user to choose again.
def get_game_difficulty():
    print("Game difficulty modes:")
    for index, difficulty in enumerate(DIFFICULTY_MAP):
        print(f"{index + 1}- {difficulty['name']} ({difficulty['mines']} mines)")

    while True:
        try:
            choice = int(input("Please choose the difficulty "))
            
            if choice < 1 or choice > len(DIFFICULTY_MAP):
                raise ValueError()

            return DIFFICULTY_MAP[choice - 1]["name"]
        except ValueError:
            print("Unknown choice")


# This function searches for the specified difficulty, and returns the associated number of mines.
# Raises a ValueError if the specified difficulty is not found in DIFFICULTY_MAP.
def get_number_of_mines(difficulty):
    for difficulty_mode in DIFFICULTY_MAP:
        if difficulty_mode["name"] == difficulty:
            return difficulty_mode["mines"]

    # validate the difficulty
    raise ValueError("Unknown difficulty")


# This function fetches the associated sizes to the specified difficulty.
# If there is only 1 size, it returns the size.
# If there are multiple sizes, it asks the user to choose the size.
# If the user inputs an unacceptable choice, the function prints an error message and asks the user to choose again.
# Returns a tuple of the form (rows, columns).
# Raises a ValueError if the specified difficulty is not found in BOARD_SIZES_MAP.
def get_board_size(difficulty):
    # validate the difficulty
    if difficulty not in BOARD_SIZES_MAP:
        raise ValueError("Unknown difficulty")
    
    # get the sizes associated with the specified difficulty
    sizes = BOARD_SIZES_MAP[difficulty]

    # Default size if there are no size choices for the specified difficulty
    selected_size = sizes[0]

    # if there are size choices, let the user choose
    if len(sizes) > 1: 
        print(f"Board sizes for {difficulty} mode:")
        for index, size in enumerate(sizes):
            print(f"{index + 1}- {size['rows']} rows * {size['columns']} columns")

        while True:
            try:
                choice = int(input("Please choose the size "))

                if choice < 1 or choice > len(sizes):
                    raise ValueError()
                
                selected_size = sizes[choice - 1]

                break
            except ValueError:
                print("Unknown choice")

    return (selected_size["rows"], selected_size["columns"])


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

            # color the cell contents
            try:
                printed_value = colored(printed_value, COLOR_MAP[printed_value])
            except KeyError:
                # don't color if mapping not found
                pass

            output += printed_value + " | "

        output_list.append(output)
        output_list.append(row_separator)

    # clear terminal and print the output
    clear_terminal()
    for output_row in output_list:
        print(output_row)


# This function returns the contents of the "fastest_times.json" file.
# If the file was not found, this function calls set_fastest_times_dictionary() to create the file 
# from "FASTEST_TIMES_TEMPLATE" and calls itself again to return the contents.
def get_fastest_times_dictionary():
    try:
        file = open(FASTEST_TIMES_FILE_PATH, "r")
        contents = file.read()
        file.close()

        return json.loads(contents)
    except FileNotFoundError:
        # create the file from the template
        set_fastest_times_dictionary(FASTEST_TIMES_TEMPLATE)

        return get_fastest_times_dictionary()


# This function creates the "fastest_times.json" file and sets "fastest_times" inside the file in a json format.
# Raises a ValueError if "fastest_times" is not a dictionary.
def set_fastest_times_dictionary(fastest_times):
    if not isinstance(fastest_times, dict):
        raise ValueError("Expected a dictionary as the parameter")

    try:
        file = open(FASTEST_TIMES_FILE_PATH, "w")
        contents = json.dumps(fastest_times)
        file.write(contents)
    finally:
        file.close()


# This function accepts 3 parameters and tries to find and return the current fastest time.
# Raises a ValueError if "difficulty" was not found.
# Raises a ValueError if "number_of_rows" and "number_of_columns" are not positive integers.
# Raises a ValueError if the size specified by "number_of_rows" and "number_of_columns" was not found.
def get_fastest_time(difficulty, number_of_rows, number_of_columns):
    # get the dictionary containing the fastest times
    fastest_times = get_fastest_times_dictionary()

    # validate the passed parameters
    if difficulty not in fastest_times:
        raise ValueError("Difficulty not found")

    if not validate_integers([number_of_rows, number_of_columns]) or number_of_rows < 0 or number_of_columns < 0:
        raise ValueError("The provided parameters for number of rows and columns should be positive integers")

    # prepare the size and get the current fastest time
    size = f"{str(number_of_rows)}*{str(number_of_columns)}"
    try:
        return fastest_times[difficulty][size]
    except KeyError:
        raise ValueError("Size not found")


# This function accepts several parameters, gets the current fastest time based on the first 3 parameters and compares
# the current fastest time with the new time which is passed as the fourth parameter.
# Returns "True" if the new time is lesser than the current fastest time, and returns "False" otherwise.
# Raises a ValueError if "difficulty" was not found.
# Raises a ValueError if "number_of_rows", "number_of_columns" and "time" are not positive integers.
# Raises a ValueError if the size specified by "number_of_rows" and "number_of_columns" was not found.
def is_fastest_time(difficulty, number_of_rows, number_of_columns, time):
    # validate the "time" parameter
    if not validate_integers([time]) or time < 0:
        raise ValueError("The provided time parameter should be a positive integer")

    # the rest of the parameters are validated by get_fastest_time()
    current_fastest_time = get_fastest_time(difficulty, number_of_rows, number_of_columns)

    return time < current_fastest_time 


# This function accepts several parameters, checks if the new time is the fastest time and sets it as the 
# current fastest time.
# Raises a ValueError if "difficulty" was not found.
# Raises a ValueError if "number_of_rows", "number_of_columns" and "time" are not positive integers.
# Raises a ValueError if the size specified by "number_of_rows" and "number_of_columns" was not found.
# Raises a ValueError if the new time is not the fastest.
def set_fastest_time(difficulty, number_of_rows, number_of_columns, time):
    # validate that the new time is the fastest time
    # params validation will also be covered
    if not is_fastest_time(difficulty, number_of_rows, number_of_columns, time):
        raise ValueError("The time provied is not the fastest time")

    # get and update the fastest_times dictionary
    fastest_times = get_fastest_times_dictionary()
    size = f"{str(number_of_rows)}*{str(number_of_columns)}"
    fastest_times[difficulty][size] = time

    # save the fastest_times dictionary
    set_fastest_times_dictionary(fastest_times)

