from functions import *

def play():
    board = create_board(16, 30, 5)

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
        can_continue = reveal_cell(board, row_index, column_index)

        if not can_continue:
            # user chose a cell with a mine, game is lost
            # print the board and show all the mines
            print_board(board, True)
            print('You Lost :(')
            break
        else:
            # user didn't lose yet
            print_board(board)
            
            # check if user won
            if is_game_won(board):
                print('You Won!! :)')
                break

            continue

play()
