# Tic Tac Toe Game in Python

## Problem Statement

This project aims to create a simple implementation of the classic Tic Tac Toe game using the Tkinter library in Python. The game allows two players to take turns placing their marks ('X' and 'O') on a 3x3 grid until one player wins by achieving a winning combination or the game ends in a draw.

## Functionalities Implemented

1. Display a graphical user interface (GUI) using the Tkinter library.
2. Allow two players to take turns and make moves on the game board.
3. Check for a winning combination or a draw to determine the game's outcome.
4. Display messages when the game ends, indicating the winner or a draw.
5. Reset the game for a new round after it concludes.

## Code Components

The code consists of the following components:

1. `TicTacToe` class: Manages the game's logic and GUI.
2. `make_move` method: Handles player moves and updates the game board.
3. `check_winner` method: Checks for a winning combination.
4. `reset_game` method: Resets the game state for a new round.
5. GUI setup: Creating the game board using buttons and arranging them in a 3x3 grid.

## Important Functions

1. `make_move(index)`: Handles player moves and updates the game board based on the selected index.
2. `check_winner()`: Checks for a winning combination among the marks on the board.
3. `reset_game()`: Resets the game state, including the board and player turn.

## Usage

To play the Tic Tac Toe game:

1. Run the code using Python.
2. The game's GUI will appear, displaying an empty 3x3 grid.
3. Players take turns clicking the empty cells to place their marks ('X' or 'O').
4. The game will automatically determine the winner or declare a draw when the game ends.
5. A message box will appear indicating the outcome, and you can click "OK" to play another round.
