import tkinter as tk
from tkinter import ttk, messagebox
from src.pet import Pet
from src.shop import ITEMS

class TamagotchiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Тамагочи – Пушок"); self.geometry("600x650"); self.configure(bg="#F5E6D3")
        self.pet = Pet("Пушок")
        self.objects = {"bed":(1,1),"food":(5,1),"toy":(1,5),"bath":(5,5)}
        self.create_widgets(); self.draw_room(); self.update_bars(); self.tick()
    def create_widgets(self):
        top = tk.Frame(self, bg="#F5E6D3"); top.pack(fill=tk.X, padx=10, pady=5)
        self.bars = {}
        for i,(l,a) in enumerate([("Голод","hunger"),("Чистота","cleanliness"),("Энергия","energy"),("Счастье","happiness")]):
            tk.Label(top, text=l, bg="#F5E6D3").grid(row=i//2, column=(i%2)*2, sticky='e')
            bar = ttk.Progressbar(top, length=120); bar.grid(row=i//2, column=(i%2)*2+1, padx=5, pady=2)
            self.bars[a]=bar
        self.coins_label = tk.Label(top, text="Монеты: 50", font=("Arial",10,"bold"), bg="#F5E6D3", fg="#D4AF37")
        self.coins_label.grid(row=1, column=4, columnspan=2, sticky='w')
        canvas_frame = tk.Frame(self, bd=3, relief=tk.SUNKEN, bg="#D2B48C")
        canvas_frame.pack(pady=5)
        self.canvas = tk.Canvas(canvas_frame, width=490, height=490, bg='white', highlightthickness=0)
        self.canvas.pack(); self.canvas.bind("<Button-1>", self.on_click)
        bottom = tk.Frame(self, bg="#F5E6D3"); bottom.pack(fill=tk.X, padx=10, pady=5)
        btns = [("Покормить",self.feed),("Помыть",self.wash),("Спать",self.sleep),("Парк",self.park),("Гардероб",self.open_wardrobe),("Магазин",self.open_shop)]
        for text,cmd in btns:
            tk.Button(bottom, text=text, command=cmd, width=10).pack(side=tk.LEFT, padx=3)
        log_frame = tk.Frame(self, bg="#F5E6D3"); log_frame.pack(fill=tk.BOTH, padx=10, pady=(0,5))
        tk.Label(log_frame, text="События:", font=("Arial",9,"bold"), bg="#F5E6D3").pack(anchor='w')
        self.log_text = tk.Text(log_frame, height=6, width=70, state=tk.DISABLED, bg="#FFF8F0", fg="#5D4E37")
        self.log_text.pack(fill=tk.BOTH)
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
                self.canvas.create_rectangle(i*70,j*70,i*70+70,j*70+70, outline='gray')
        for obj,(x,y) in self.objects.items():
            self.canvas.create_text(x*70+35, y*70+35, text=obj[0].upper())
        emoji = ITEMS[self.pet.outfit]["emoji"] if self.pet.outfit else "🐱"
        px,py = self.pet.position
        self.canvas.create_text(px*70+35, py*70+35, text=emoji, font=("Arial",24))
    def on_click(self, event):
        col,row = event.x//70, event.y//70
        if 0<=col<7 and 0<=row<7:
            self.pet.position = (col,row)
            self.draw_room()
    def open_shop(self): pass
    def open_wardrobe(self): pass
    def tick(self): self.after(5000, self.tick)
