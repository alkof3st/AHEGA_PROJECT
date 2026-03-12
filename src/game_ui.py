import tkinter as tk

class TamagotchiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Тамагочи – Пушок")
        self.objects = {"bed":(1,1),"food":(5,1),"toy":(1,5),"bath":(5,5)}
        self.canvas = tk.Canvas(self, width=420, height=420, bg='white')
        self.canvas.pack()
        self.draw_room()
    def draw_room(self):
        self.canvas.delete("all")
        for i in range(7):
            for j in range(7):
                x1,y1 = i*60, j*60
                self.canvas.create_rectangle(x1,y1,x1+60,y1+60, outline='gray')
        for obj, (x,y) in self.objects.items():
            self.canvas.create_text(x*60+30, y*60+30, text=obj[0].upper())
