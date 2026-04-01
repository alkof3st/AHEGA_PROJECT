import tkinter as tk
from tkinter import ttk, messagebox
from src.pet import Pet
from src.shop import ITEMS

class TamagotchiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Тамагочи – Пушок")
        self.pet = Pet("Пушок")
        self.objects = {"bed":(1,1),"food":(5,1),"toy":(1,5),"bath":(5,5)}
        self.create_widgets()
        self.draw_room()
    # ... (реализованы методы open_shop и open_wardrobe с диалогами)
    def open_shop(self):
        win = tk.Toplevel(self); win.title("Магазин")
        for name, data in ITEMS.items():
            f = tk.Frame(win); f.pack(fill=tk.X)
            tk.Label(f, text=f"{data['emoji']} {name} - {data['price']}💰").pack(side=tk.LEFT)
            btn = tk.Button(f, text="Купить", command=lambda n=name, p=data['price']: self.buy_item(n,p))
            if name in self.pet.inventory: btn.config(state=tk.DISABLED, text="Куплено")
            btn.pack(side=tk.RIGHT)
    def buy_item(self, name, price):
        if self.pet.buy(name, price):
            messagebox.showinfo("Магазин", f"Куплено: {name}")
            self.update_bars()
    def open_wardrobe(self):
        win = tk.Toplevel(self); win.title("Гардероб")
        for item in self.pet.inventory:
            f = tk.Frame(win); f.pack(fill=tk.X)
            tk.Label(f, text=f"{ITEMS[item]['emoji']} {item}").pack(side=tk.LEFT)
            tk.Button(f, text="Надеть", command=lambda i=item: self.wear_outfit(i)).pack(side=tk.RIGHT)
    def wear_outfit(self, item):
        self.pet.outfit = item; self.draw_room()
