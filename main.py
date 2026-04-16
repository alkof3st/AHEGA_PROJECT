import json, os
from src.game_ui import TamagotchiApp

SAVE_FILE = "save.json"

def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def save_game(data):
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    saved = load_game()
    app = TamagotchiApp(saved)
    app.protocol("WM_DELETE_WINDOW", lambda: (save_game(app.get_save_data()), app.destroy()))
    app.mainloop()
