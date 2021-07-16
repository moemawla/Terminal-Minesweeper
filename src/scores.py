from functions import *


def show_scores():    
    print_banner()

    fastest_times = get_fastest_times_dictionary()

    print("The current fastest times:")
    print("**************************")
    for difficulty, sizes in fastest_times.items():
        for size, time in sizes.items():
            print(f"Fastest time for {difficulty} mode and {size} board is {time} seconds.")
    print("", end="\n\n")


show_scores()
