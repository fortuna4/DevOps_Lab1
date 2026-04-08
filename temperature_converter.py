import tkinter as tk
from tkinter import ttk, messagebox

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Конвертер температур")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Заголовок
        title_label = tk.Label(root, text="Конвертер температур", 
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Основной фрейм
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill="both", expand=True)
        
        # Ввод температуры
        ttk.Label(main_frame, text="Введите температуру:", 
                  font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=5)
        self.temp_entry = ttk.Entry(main_frame, font=("Arial", 11), width=15)
        self.temp_entry.grid(row=0, column=1, pady=5, padx=10)
        
        # Выбор исходной шкалы
        ttk.Label(main_frame, text="Исходная шкала:", 
                  font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=5)
        self.from_scale = ttk.Combobox(main_frame, values=["Цельсий", "Фаренгейт", "Кельвин"], 
                                       state="readonly", width=12)
        self.from_scale.grid(row=1, column=1, pady=5, padx=10)
        self.from_scale.set("Цельсий")
        
        # Выбор целевой шкалы
        ttk.Label(main_frame, text="Целевая шкала:", 
                  font=("Arial", 11)).grid(row=2, column=0, sticky="w", pady=5)
        self.to_scale = ttk.Combobox(main_frame, values=["Цельсий", "Фаренгейт", "Кельвин"], 
                                     state="readonly", width=12)
        self.to_scale.grid(row=2, column=1, pady=5, padx=10)
        self.to_scale.set("Фаренгейт")
        
        # Кнопка конвертации
        convert_btn = ttk.Button(main_frame, text="Конвертировать", 
                                 command=self.convert_temperature)
        convert_btn.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Результат
        self.result_label = tk.Label(main_frame, text="", font=("Arial", 14, "bold"), 
                                     fg="blue")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Дополнительная информация
        info_frame = ttk.LabelFrame(root, text="Справка", padding="10")
        info_frame.pack(fill="x", padx=20, pady=10)
        
        info_text = """
        Формулы конвертации:
        • Цельсий → Фаренгейт: (°C × 9/5) + 32
        • Цельсий → Кельвин: °C + 273.15
        • Фаренгейт → Цельсий: (°F - 32) × 5/9
        • Фаренгейт → Кельвин: (°F - 32) × 5/9 + 273.15
        • Кельвин → Цельсий: K - 273.15
        • Кельвин → Фаренгейт: (K - 273.15) × 9/5 + 32
        """
        
        info_label = tk.Label(info_frame, text=info_text, font=("Arial", 9), 
                              justify="left")
        info_label.pack()
    
    def convert_temperature(self):
        try:
            # Получаем значение температуры
            temp_value = float(self.temp_entry.get())
            from_scale = self.from_scale.get()
            to_scale = self.to_scale.get()
            
            # Конвертация
            result = self.convert(temp_value, from_scale, to_scale)
            
            # Отображение результата
            self.result_label.config(
                text=f"{temp_value}°{self.get_symbol(from_scale)} = {result:.2f}°{self.get_symbol(to_scale)}"
            )
            
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректное число!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
    
    def convert(self, value, from_scale, to_scale):
        # Сначала конвертируем в Цельсий
        if from_scale == "Цельсий":
            celsius = value
        elif from_scale == "Фаренгейт":
            celsius = (value - 32) * 5/9
        elif from_scale == "Кельвин":
            celsius = value - 273.15
        else:
            raise ValueError("Неизвестная шкала")
        
        # Конвертируем из Цельсия в нужную шкалу
        if to_scale == "Цельсий":
            return celsius
        elif to_scale == "Фаренгейт":
            return celsius * 9/5 + 32
        elif to_scale == "Кельвин":
            return celsius + 273.15
        else:
            raise ValueError("Неизвестная шкала")
    
    def get_symbol(self, scale):
        symbols = {
            "Цельсий": "C",
            "Фаренгейт": "F",
            "Кельвин": "K"
        }
        return symbols.get(scale, "")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()