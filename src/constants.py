ACCEPTED_CELL_VALUES = {" ", "*", "#", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8"}

BOARD_SIZE_MAP = {
    "Beginner": [
        {"rows": 8, "columns": 8},
        {"rows": 9, "columns": 9},
        {"rows": 10, "columns": 10}
    ],
    "Intermediate": [
        {"rows": 13, "columns": 15},
        {"rows": 16, "columns": 16}
    ],
    "Expert": [
        {"rows": 16, "columns": 30}
    ]
}

CHARACTERS = "abcdefghijklmnop"

DIFFICULTY_MAP = {1: "Beginner", 2: "Intermediate", 3: "Expert"}

FLAG_MAP = {" ": "F", "F": " ", "*": "#", "#": "*", "0": "0", "1": "1",
 "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8"}

PRINT_MAP = {" ": " ", "*": " ", "#": "F", "F": "F", "0": "0", "1": "1",
 "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8"}
