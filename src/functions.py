def validate_integers(integers, error_message):
    for integer in integers:
        if not isinstance(integer, int):
            raise ValueError(error_message)
