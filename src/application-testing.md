# First Test
### This test covers the "fastest times" or "scores" feature.

| Scenario | Expected behavior | Actual behavior | Status |
| -------- | ----------------- | --------------- | ------ |
| Calling "./minesweeper.sh scores" | Should return the results from "./src/fastest_times.json" | As expected | Passed |
| Calling "./minesweeper.sh scores" when "./src/fastest_times.json" is not found | Should create the file from the template dictionary and return the results | As expected | Passed |
| Calling "./minesweeper.sh scores" after winning a game and acheiving a fastest time | Should return the results with the updated fastest time | As expected | Passed |

<br/>

# Second Test
### This test covers the "choosing game difficulty" and "choosing board size" features.

| Scenario | Expected behavior | Actual behavior | Status |
| -------- | ----------------- | --------------- | ------ |
| Calling "./minesweeper.sh play" | Should launch the game and ask user to choose difficulty | As expected | Passed |
| What difficulty options are supplied to the user to choose from? | Should show 3 options: "Beginner", "Intermediate" and "Expert" | As expected | Passed |
| What happens if the user inputs a wrong number when asked to choose a difficulty? | Should return an error message and ask for a choice again | As expected | Passed |
| What happens if the user chooses "Beginner"? | Should proceed to asking the user to choose 1 of 3 board sizes | As expected | Passed |
| What happens if the user chooses "Intermediate"? | Should proceed to asking the user to choose 1 of 2 board sizes | As expected | Passed |
| What happens if the user chooses "Expert"? | Should not ask the user to choose a board size | As expected | Passed |
| What happens if the user inputs a wrong number when asked to choose a size? | Should return an error message and ask for a choice again | As expected | Passed |
| What happens after the size is picked? | Should display the instructions on how to play and ask the user to press any key to start playing | As expected | Passed |
| What happens after the user presses any key when the game instructions are displayed? | Should print a board with the specified size and ask the user for an instruction | As expected | Passed |
| What happens if the user presses "ctrl + c" at anytime during the game? | Should exit gracefully and print "Bye!" | As expected | Passed |
