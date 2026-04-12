import tkinter as tk
from tkinter import messagebox
import random

class RouletteGame:
    def __init__(self, app):
        self.app = app
        self.top = tk.Toplevel(app)
        self.top.title("Рулетка")
        tk.Label(self.top, text="Ставка (монет):").pack(pady=5)
        self.bet_entry = tk.Entry(self.top, font=("Arial",12))
        self.bet_entry.pack(pady=5)
        tk.Label(self.top, text="Число (1-10):").pack(pady=5)
        self.num_entry = tk.Entry(self.top, font=("Arial",12))
        self.num_entry.pack(pady=5)
        tk.Button(self.top, text="Крутить!", command=self.spin).pack(pady=10)
    def spin(self):
        try:
            bet = int(self.bet_entry.get())
            if bet <= 0 or bet > self.app.pet.coins:
                messagebox.showerror("Ошибка", "Некорректная ставка."); return
            num = int(self.num_entry.get())
            if num < 1 or num > 10:
                messagebox.showerror("Ошибка", "Число должно быть 1-10."); return
        except ValueError:
            messagebox.showerror("Ошибка", "Введите числа."); return
        self.app.pet.coins -= bet
        result = random.randint(1,10)
        if result == num:
            win = bet * 2
            self.app.pet.add_coins(win)
            messagebox.showinfo("Удача!", f"Выпало {result}! Выигрыш {win}💰")
        else:
            messagebox.showinfo("Неудача", f"Выпало {result}. Ставка {bet}💰 потеряна.")
        self.app.update_bars()
        self.top.destroy()
