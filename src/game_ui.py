import tkinter as tk
from tkinter import ttk, messagebox
import os, json
from src.pet import Pet
from src.shop import ITEMS
from src.minigames.word_game import WordGame
from src.minigames.tic_tac_toe import TicTacToeGame
from src.minigames.roulette import RouletteGame

try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

def load_image(name, size=None):
    if not os.path.isdir(ASSETS_DIR): return None
    path = os.path.join(ASSETS_DIR, name)
    if not os.path.exists(path): return None
    try:
        if PIL_AVAILABLE:
            img = Image.open(path)
            if size: img = img.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
        else:
            if path.lower().endswith('.gif') and not size: return tk.PhotoImage(file=path)
            return None
    except Exception: return None
