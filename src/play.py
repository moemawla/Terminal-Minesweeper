from functions import *
import time


def play():
    print_banner()
    
    try:
        # get the game difficulty and board size
        difficulty = get_game_difficulty()
        board_size = get_board_size(difficulty)
        number_of_rows = board_size[0]
        number_of_columns = board_size[1]

        # create the board
        board = create_board(number_of_rows, number_of_columns, get_number_of_mines(difficulty))

        # print game instructions
        print('''
Game Instructions:
1- To choose a cell pass its row and column indices without a space (ex: b5)
2- To flag or unflag a cell, type "flag" followed by a space and then the cell's location (ex: flag b5)
3- To leave game type "exit"
        ''')
        input("Press any key to start!")

        # start tracking time
        start_time = time.time()
        print_board(board)
    except KeyboardInterrupt:
        print("Bye!")
        return

    while True:
        try:
            choice = get_user_choice(board)

            # check if user wants to exit the game
            if choice == None:
                print("Bye!")
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

            # check if user chose a cell with a mine, game is lost 
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
        print("You Won!! :)")

        if is_fastest_time(difficulty, number_of_rows, number_of_columns, total_time):
            set_fastest_time(difficulty, number_of_rows, number_of_columns, total_time)
            print(f"You got the fastest time for {difficulty} mode and {number_of_rows}*{number_of_columns} size with {total_time} seconds!!")
        else:
            print(f"You finished in {total_time} seconds")
    else:
        print("You Lost :(")


play()
