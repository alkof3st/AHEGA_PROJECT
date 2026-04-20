# ... (добавлен метод save_progress и кнопка «Сохранить»)
    def save_progress(self):
        data = self.get_save_data()
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        self.log("Прогресс сохранён.")
