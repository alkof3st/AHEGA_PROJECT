import tkinter as tk
from tkinter import messagebox
import random

class WordGame:
    def __init__(self, app):
        self.app = app
        self.top = tk.Toplevel(app)
        self.top.title("Угадай слово")
        self.words = ["КОТ","ПИТОМЕЦ","ТАМАГОЧИ","ИГРА"]
        self.secret = random.choice(self.words).upper()
        self.guessed = set()
        self.errors = 0
        self.max_errors = 6
        self.label_word = tk.Label(self.top, text=self.get_display_word(), font=("Courier",20))
        self.label_word.pack(pady=10)
        self.entry = tk.Entry(self.top, font=("Arial",14))
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", lambda e: self.guess())
        tk.Button(self.top, text="Угадать", command=self.guess).pack(pady=5)
    def get_display_word(self):
        return " ".join([ch if ch in self.guessed else "_" for ch in self.secret])
    def guess(self):
        letter = self.entry.get().upper()
        self.entry.delete(0, tk.END)
        if letter in self.guessed: return
        self.guessed.add(letter)
        if letter not in self.secret:
            self.errors += 1
        self.label_word.config(text=self.get_display_word())
        if all(ch in self.guessed for ch in self.secret):
            messagebox.showinfo("Победа!", "Вы угадали слово!")
            self.top.destroy()
        elif self.errors >= self.max_errors:
            messagebox.showinfo("Поражение", f"Слово: {self.secret}")
            self.top.destroy()
