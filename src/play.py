from functions import *
from termcolor import colored
import time


def play(): 
    # initialize the board
    try:
        # get the game difficulty
        print_banner()
        difficulty = get_game_difficulty()

        # get the board size
        print_banner()
        board_size = get_board_size(difficulty)

        # create the board
        number_of_rows = board_size[0]
        number_of_columns = board_size[1]
        board = create_board(number_of_rows, number_of_columns, get_number_of_mines(difficulty))

        # print game instructions
        print_game_instructions()

        # start tracking time
        start_time = time.time()
        print_board(board)
    except KeyboardInterrupt:
        print("\nBye!\n")
        return

    # start the actual gameplay
    while True:
        try:
            choice = get_user_choice(board)

            # check if user wants to exit the game
            if choice == None:
                print("\nBye!\n")
                return
        except ValueError as e:
            print(str(e))
            continue

        # user input is valid, process it
        row_index = choice[0]
        column_index = choice[1]
        operation = choice[2]

        if operation == "reveal":
            can_continue = reveal_cell(board, row_index, column_index)

            # check if the user chose a cell with a mine, game is lost 
            if not can_continue:
                break

            # check if user won
            if is_game_won(board):
                break
        else:
            flag_cell(board, row_index, column_index)

        # game didn't end yet, print the updated board
        print_board(board)

    # game ended, stop tracking time
    total_time = int(time.time() - start_time)
    
    # print board and show the mines
    print_board(board, True)

    # check if game is won or lost
    if is_game_won(board):
        print(colored("You Won!! :)", "green"))

        if is_fastest_time(difficulty, number_of_rows, number_of_columns, total_time):
            set_fastest_time(difficulty, number_of_rows, number_of_columns, total_time)
            print(f"You got the fastest time for {difficulty} mode and {number_of_rows}*{number_of_columns} size with {total_time} seconds!!")
        else:
            print(f"You finished in {total_time} seconds")
    else:
        print(colored("You Lost :(", "red"))

    print("", end="\n\n")


play()
