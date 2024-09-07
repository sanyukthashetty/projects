# 🎮 Tic Tac Toe Game in Python

## 📋 Project Overview
This project is a simple implementation of the classic Tic Tac Toe game, built using the Tkinter library in Python. It allows two players to take turns marking their symbols ('X' and 'O') on a 3x3 grid. The game continues until one player wins by achieving a winning combination or the game ends in a draw.

## ✨ Features
- **🎨 Graphical User Interface (GUI):** The game features an intuitive GUI developed with Tkinter.
- **👥 Two-Player Mode:** Players take turns to make their moves on the game board.
- **🏆 Winning and Draw Detection:** The game automatically checks for a winning combination or a draw.
- **🔄 Game Reset:** Players can easily reset the game to start a new round after it concludes.
- **📣 Interactive Feedback:** The game displays messages to indicate the winner or if the game ends in a draw.

## 🛠 Code Components

The code consists of the following key components:

1. **`TicTacToe` class:** Manages the game logic and GUI elements.
2. **`make_move` method:** Handles player moves and updates the game board accordingly.
3. **`check_winner` method:** Evaluates the board for any winning combination.
4. **`reset_game` method:** Resets the game state for a new round.
5. **GUI setup:** Creates and arranges the game board using buttons in a 3x3 grid.

## 🔑 Key Functions

- **`make_move(index):`** Processes player moves, updates the board, and checks for game termination conditions.
- **`check_winner():`** Checks for a winning combination based on the current state of the board.
- **`reset_game():`** Resets the board and player turn to start a new game.

## 🎲 Game Rules
1. The game is played on a 3x3 grid.
2. Players alternate turns, with one using 'X' and the other 'O'.
3. A player wins by placing three of their marks in a horizontal, vertical, or diagonal row.
4. If all cells are filled and no player has won, the game ends in a draw.

## 🚀 How to Play

1. Run the code using Python.
2. The game's GUI will appear, displaying an empty 3x3 grid.
3. Players take turns clicking the empty cells to place their marks ('X' or 'O').
4. The game will automatically determine the winner or declare a draw when the game ends.
5. A message box will appear indicating the outcome, and you can click "OK" to reset the game for a new round.

## 📝 Additional Information

This project was developed by **Sanyuktha Shetty** on **14-08-2023** as part of a learning exercise at MITE. It leverages Python’s Tkinter library to create an engaging and interactive user experience.
