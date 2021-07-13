def validate_integers(integers, error_message):
    for integer in integers:
        if not isinstance(integer, int):
            raise ValueError(error_message)

def get_number_of_rows(board):
    return len(board)

def get_number_of_columns(board):
    return len(board[0])
