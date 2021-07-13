from functions import *

def play():
    board = create_board(16, 30, 5)
    #print_board(board)
    print(get_user_choice(board))

play()