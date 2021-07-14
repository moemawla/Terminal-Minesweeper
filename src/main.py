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

    #print_board(board)

play()