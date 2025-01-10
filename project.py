import tkinter as tk
from tkinter import messagebox

def check_win(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True

    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")

        
        self.board = [[" "] * 3 for _ in range(3)]
        self.players = ["X", "O"]
        self.current_player = 0  

        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text=" ", font=("Arial", 24), width=5, height=2,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.players[self.current_player]
            self.buttons[row][col].config(text=self.players[self.current_player])

            
            if check_win(self.board, self.players[self.current_player]):
                messagebox.showinfo("Game Over", f"Player {self.players[self.current_player]} wins!")
                self.reset_game()
            elif is_board_full(self.board):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = 1 - self.current_player
        else:
            messagebox.showwarning("Invalid Move", "This position is already taken. Choose another.")

    def reset_game(self):
        self.board = [[" "] * 3 for _ in range(3)]
        self.current_player = 0
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")

    def run(self):
    
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
