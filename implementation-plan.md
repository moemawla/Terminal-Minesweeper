# Implementation plan:
### The below table lists all the tasks needed to finalize the application with all the proposed features. The tasks are ordered based on priority from highest to lowest.

| Item | Feature | Due Date |
| ---- | ------- | -------- |
| Create the basic code that creates a board with randomly positioned mines inside | Implement the basic game with the flagging feature | July 14 |
| The application should display the board in the terminal | Implement the basic game with the flagging feature | July 14 |
| The application should interact with the user to accept a choice of a box | Implement the basic game with the flagging feature | July 14 |
| The application should validate the choice, print an error message if the user inputs wrong choice and ask the user to choose again | Implement the basic game with the flagging feature | July 14 |
| The application should process the user's choices and display the correct information on the board | Implement the basic game with the flagging feature | July 14 |
| The application should allow the user to flag or unflag boxes in the board. | Implement the basic game with the flagging feature | July 14 |
| The application should ask the user for the desired difficulty at the start | Implement the game difficulty feature | July 15 |
| The application should validate the choice, print an error message if the user inputs wrong choice and ask the user to choose again | Implement the game difficulty feature | July 15 |
| The application should set the number of mines based on the chosen difficulty | Implement the game difficulty feature | July 15 |
| The application should ask the user for the desired board size | Implement the board size feature | July 15 |
| The application should validate the choice, print an error message if the user inputs wrong choice and ask the user to choose again | Implement the board size feature | July 15 |
| The application should create the board based on the chosen size | Implement the board size feature | July 15 |
| Let the application track the time taken to finish the game | Implement the highest scores feature | July 15 |
| When the user wins a game, fetch the highest score for the current game size and difficulty from the scores file | Implement the highest scores feature | July 15 |
| Update the scores file If the user won the game in less time than the highest score | Implement the highest scores feature | July 15 |
| Print on the screen to notify the user if he got the current highest score | Implement the highest scores feature | July 15 |
| The application should not break If the scores file was not found, and instead a new file should be created | Implement the highest scores feature | July 15 |
| The bash script should make sure that the environment has all the needed services and python installed | Wrap the application with a bash script | July 16 |
| The bash script should accept a single required argument. If the user passes a wrong, or no, argument the script should return a clear message and print "Run the script with the 'help' argument for list of possible arguments" | Wrap the application with a bash script | July 16 |
| If the user inputs 'help' for the required argument, the bash script will return a list of the 3 possible options for the argument ("help", "play" and "scores") | Wrap the application with a bash script | July 16 |
| If the user inputs 'play' for the required argument, the bash script will call the python module responsible for starting the game | Wrap the application with a bash script | July 16 |
| If the user inputs 'scores' for the required argument, the bash script will call the python module responsible for printing the current highest scores | Wrap the application with a bash script | July 16 |
