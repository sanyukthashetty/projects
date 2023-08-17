import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.turn = "X"
        self.board = [""] * 9

        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text="", font=("Helvetica", 24), height=2, width=6, command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.turn
            self.buttons[index].config(text=self.turn)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.turn} wins!")
                self.reset_game()
            elif all(cell != "" for cell in self.board):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.turn = "O" if self.turn == "X" else "X"

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def reset_game(self):
        self.turn = "X"
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

