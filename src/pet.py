from src.utils import clamp

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger=50; self.cleanliness=50; self.energy=50; self.happiness=50
        self.coins=50; self.inventory=[]; self.outfit=None; self.position=(3,3); self.alive=True; self.sick=False
    def feed(self): self.hunger = clamp(self.hunger+25,0,100)
    def wash(self): self.cleanliness = clamp(self.cleanliness+30,0,100); self.coins+=5; self.sick=False
    def sleep(self): self.energy = 100; self.sick=False
    def play(self):
        if self.energy < 20: return False
        self.energy-=25; self.cleanliness-=20; self.happiness=clamp(self.happiness+30,0,100); self.coins+=10; return True
    def buy(self, item, price):
        if self.coins >= price and item not in self.inventory:
            self.coins -= price; self.inventory.append(item); return True
        return False
    def tick(self):
        self.hunger = clamp(self.hunger-1,0,100); self.cleanliness = clamp(self.cleanliness-1,0,100)
        self.energy = clamp(self.energy-1,0,100); self.happiness = clamp(self.happiness-1,0,100)
        if self.cleanliness<20 and not self.sick: self.sick=True
        if self.sick:
            self.energy = clamp(self.energy-1,0,100); self.happiness = clamp(self.happiness-1,0,100)
