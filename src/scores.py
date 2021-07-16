from functions import *


def show_scores():
    fastest_times = get_fastest_times_dictionary()
    
    clear_terminal()
    print("The current fastest times:")
    print("**************************")
    for difficulty, sizes in fastest_times.items():
        for size, time in sizes.items():
            print(f"Fastest time for {difficulty} mode and {size} board is {time} seconds.")


show_scores()
