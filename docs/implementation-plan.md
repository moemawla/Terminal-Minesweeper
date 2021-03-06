# Implementation plan
### The below table lists all the tasks needed to finalize the application with all the proposed features. The tasks are ordered based on priority from highest to lowest.

| Task | Feature/Scope | Due Date |
| ---- | ------- | -------- |
| Create the basic code that creates a board with randomly positioned mines inside | Implement the basic game with the flagging feature | July 14 |
| The application should display the board in the terminal | Implement the basic game with the flagging feature | July 14 |
| The application should interact with the user to accept a choice of a box | Implement the basic game with the flagging feature | July 14 |
| The application should validate the choice, print an error message if the user inputs wrong choice and ask the user to choose again | Implement the basic game with the flagging feature | July 14 |
| The application should process the user's choices and display the correct information on the board | Implement the basic game with the flagging feature | July 14 |
| The application should allow the user to flag or unflag boxes in the board. | Implement the basic game with the flagging feature | July 14 |
| The application should ask the user for the desired difficulty at the start | Implement the game difficulty feature | July 15 |
| The application should validate the choice, print an error message if the user inputs wrong choice and ask the user to choose again | Implement the game difficulty feature | July 15 |
| If the user chooses the "Beginner" mode, the application should add 10 mines to the board | Implement the game difficulty feature | July 15 |
| If the user chooses the "Intermediate" mode, the application should add 40 mines to the board | Implement the game difficulty feature | July 15 |
| If the user chooses the "Expert" mode, the application should add 99 mines to the board | Implement the game difficulty feature | July 15 |
| The application should ask the user for the desired board size | Implement the board size feature | July 15 |
| The application should validate the choice, print an error message if the user inputs wrong choice and ask the user to choose again | Implement the board size feature | July 15 |
| If the difficulty mode is "Beginner", the allowed sizes are 8 ?? 8, 9 ?? 9, or 10 ?? 10 | Implement the board size feature | July 15 |
| If the difficulty mode is "Intermediate", the allowed sizes are 13 ?? 15 or 16 ?? 16 | Implement the board size feature | July 15 |
| If the difficulty mode is "Expert", the size is always 16 ?? 30 | Implement the board size feature | July 15 |
| The application should track the time taken to finish the game. | Implement the fastest times (scores) feature | July 16 |
| When the user wins a game, fetch the fastest time for the current game size and difficulty from the fastest_times file | Implement the fastest times (scores) feature | July 16 |
| The application should not break if the fastest_times file was not found and a new file should be created instead. | Implement the fastest times (scores) feature | July 16 |
| Update the fastest_times file If the user won the game in less time than the current fastest time | Implement the fastest times (scores) feature | July 16 |
| Print on the screen to notify the user if he got the current fastest time | Implement the fastest times (scores) feature | July 16 |
| Calling the scores module will print the current fastest times per board size and difficulty | Implement the fastest times (scores) feature | July 16 |
| The bash script should make sure that the environment has all the needed services and python installed | Wrap the application with a bash script | July 16 |
| The bash script should accept a single required argument. If the user passes a wrong, or no, argument the script should return a clear message and print "Run the script with the 'help' argument for list of possible arguments" | Wrap the application with a bash script | July 16 |
| If the user inputs 'help' for the required argument, the bash script will return a list of the 3 possible options for the argument ("help", "play" and "scores") | Wrap the application with a bash script | July 16 |
| If the user inputs 'play' for the required argument, the bash script will call the python module responsible for starting the game | Wrap the application with a bash script | July 16 |
| If the user inputs 'scores' for the required argument, the bash script will call the python module responsible for printing the current fastest times | Wrap the application with a bash script | July 16 |

<br/><br/>

# Extra features
### After finalizing all the features in the implementation plan above, I found that I have enough time to implement the following cool extra features:
1. Implement absolute paths in the bash scripts to allow the application to work from anywhere it was ran from.
2. Add ASCII art banner to the game.
3. Print the board cells in different colors depending on their contents, which will drastically improve how the user can view and analyse the board.
4. The above feature, "Print the board cells in colors", required a third party package to be used which gave me the oppurtunity to use "virtualenv" and increase the complexity of the bash script that is responsible for preparing the environment.
