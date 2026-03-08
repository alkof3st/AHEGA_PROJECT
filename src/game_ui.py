import tkinter as tk

class TamagotchiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Тамагочи – Пушок")
        self.canvas = tk.Canvas(self, width=420, height=420, bg='white')
        self.canvas.pack()
        self.draw_grid()
    def draw_grid(self):
        for i in range(7):
            for j in range(7):
                x1,y1 = i*60, j*60
                self.canvas.create_rectangle(x1,y1,x1+60,y1+60, outline='gray')
