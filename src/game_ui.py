import tkinter as tk
from tkinter import ttk
from src.pet import Pet

class TamagotchiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Тамагочи – Пушок")
        self.pet = Pet("Пушок")
        self.objects = {"bed":(1,1),"food":(5,1),"toy":(1,5),"bath":(5,5)}
        self.create_widgets()
        self.draw_room()
    def create_widgets(self):
        top = tk.Frame(self); top.pack(fill=tk.X)
        self.bars = {}
        for i, (label, attr) in enumerate([("Голод","hunger"),("Чистота","cleanliness"),("Энергия","energy"),("Счастье","happiness")]):
            ttk.Label(top, text=label).grid(row=i//2, column=(i%2)*2)
            bar = ttk.Progressbar(top, length=100); bar.grid(row=i//2, column=(i%2)*2+1)
            self.bars[attr]=bar
        self.coins_label = ttk.Label(top, text="Монеты: 50"); self.coins_label.grid(row=1, column=4)
        self.canvas = tk.Canvas(self, width=420, height=420, bg='white'); self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        bottom = tk.Frame(self); bottom.pack(fill=tk.X)
        tk.Button(bottom, text="Покормить", command=self.feed).pack(side=tk.LEFT)
        tk.Button(bottom, text="Помыть", command=self.wash).pack(side=tk.LEFT)
        tk.Button(bottom, text="Спать", command=self.sleep).pack(side=tk.LEFT)
        tk.Button(bottom, text="Парк", command=self.park).pack(side=tk.LEFT)
    def feed(self): self.pet.feed(); self.update_bars()
    def wash(self): self.pet.wash(); self.update_bars()
    def sleep(self): self.pet.sleep(); self.update_bars()
    def park(self): self.pet.play(); self.update_bars()
    def update_bars(self):
        for attr, bar in self.bars.items():
            bar['value'] = getattr(self.pet, attr)
        self.coins_label.config(text=f"Монеты: {self.pet.coins}")
    def draw_room(self):
        self.canvas.delete("all")
        for i in range(7):
            for j in range(7):
                self.canvas.create_rectangle(i*60,j*60,i*60+60,j*60+60, outline='gray')
        for obj,(x,y) in self.objects.items():
            self.canvas.create_text(x*60+30, y*60+30, text=obj[0].upper())
        px,py = self.pet.position
        self.canvas.create_text(px*60+30, py*60+30, text="🐱", font=("Arial",24))
    def on_click(self, event):
        col,row = event.x//60, event.y//60
        if 0<=col<7 and 0<=row<7:
            self.pet.position = (col,row)
            self.draw_room()
