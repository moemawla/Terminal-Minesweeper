from functions import *

def play():
    try:
        # get the game difficulty and board size
        difficulty = get_game_difficulty()
        board_size = get_board_size(difficulty)

        # create the board
        board = create_board(board_size[0], board_size[1], get_number_of_mines(difficulty))

        # print game instructions
        print('''
Game Instructions:
1- To choose a cell pass its row and column indices without a space (ex: b5)
2- To flag or unflag a cell, type "flag" followed by a space and then the cell's location (ex: flag b5)
3- To leave game type "exit"
        ''')
        input("Press any key to start!")
        clear_terminal()
        print_board(board)
    except KeyboardInterrupt:
        print('Bye!')
        return

    while True:
        try:
            choice = get_user_choice(board)

            # check if user wants to exit the game
            if choice == None:
                print('Bye!')
                return
        except ValueError as e:
            print(str(e))
            continue

        # user input is valid, process it
        row_index = choice[0]
        column_index = choice[1]
        operation = choice[2]

        if operation == 'reveal':
            can_continue = reveal_cell(board, row_index, column_index)
        else:
            can_continue = True
            flag_cell(board, row_index, column_index)

        if not can_continue:
            # user chose a cell with a mine, game is lost
            # print the board and show all the mines
            clear_terminal()
            print_board(board, True)
            print('You Lost :(')
            break
        else:
            # user didn't lose yet
            clear_terminal()
            print_board(board)

            # check if user won
            if is_game_won(board):
                print('You Won!! :)')
                break

play()
