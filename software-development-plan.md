# Statement of Purpose and Scope
This application is a minesweeper game that users can launch and play in the terminal.
The game will allow the user to input choices of boxes from the board. If the user chooses a box that contains a mine, the user loses the game. If the user chooses a box that has no bomb, the application will open the box with a number inside it indicating how many bombs are around the box. If there are no bombs around the chosen box, the application will automatically open all boxes immediately surrounding the box.
Any person will be able to run the application with the help of the provided instructions.

# Features
The application will have the following features:
- Option to flag or unflag boxes:
    * This feature would be directly available inside the game by passing a certain input.
    * A flagged box would indicate to the user that the box contains a mine.
    * This will make it easier for users to ignore boxes they aleady analyzed.
- Option to select game difficulty (chosen by the user at the beginning of the game, after the app launches):
    * Beginner has 10 mines.
    * Intermediate has 40 mines.
    * Expert has 99 mines.
- Option to select board size (chosen by the user at the beginning of the game, after the app launches):
    * For beginner mode, the board size is either 8 × 8, 9 × 9, or 10 × 10.
    * For intermediate mode, the board size is either 13 × 15 or 16 × 16.
    * For expert mode, the board size is always 16 × 30.
- Option to show fastest times or scores (chosen by the user as an argument to the script):
    * These scores will be based on fastest time per game size and difficulty.
    * The scores will be written to, or read from, a separate file.

# User Interaction and Experience
- The user can read the help file provided to undersatand how to start using the application and what are the possible arguments.
- The user can also call the script with the "help" argument which will return a list of all possible arguments and their descriptions.
- When the user runs the script with the "play" argument, the game is launched and the user can choose the difficulty and board size.
- When the user runs the script with "scores" argument, the application will print the current fastest times to the terminal.
- The application should not break if a user passes wrong, or no, arguments and instead should return an error message saying that the argument provided is not supported and print "Run the script with the 'help' argument for a list of possible arguments".


# Control Flow Diagram


