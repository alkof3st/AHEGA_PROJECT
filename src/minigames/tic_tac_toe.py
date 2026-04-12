import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGame:
    def __init__(self, app):
        self.app = app
        self.top = tk.Toplevel(app)
        self.top.title("Крестики-нолики")
        self.board = [""]*9
        self.buttons = []
        for i in range(9):
            btn = tk.Button(self.top, text="", font=("Arial",20), width=3, height=1,
                            command=lambda idx=i: self.player_move(idx))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)
    def player_move(self, idx):
        if self.board[idx] != "": return
        self.board[idx] = "X"; self.buttons[idx].config(text="X", state=tk.DISABLED)
        if self.check_win("X"): messagebox.showinfo("Победа!", "Вы выиграли!"); self.top.destroy(); return
        if "" not in self.board: messagebox.showinfo("Ничья", "Ничья!"); self.top.destroy(); return
        self.computer_move()
    def computer_move(self):
        empty = [i for i,v in enumerate(self.board) if v==""]
        move = random.choice(empty)
        self.board[move] = "O"; self.buttons[move].config(text="O", state=tk.DISABLED)
        if self.check_win("O"): messagebox.showinfo("Поражение", "Компьютер выиграл."); self.top.destroy()
    def check_win(self, player):
        wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        return any(self.board[a]==self.board[b]==self.board[c]==player for a,b,c in wins)
