import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import random

plants_data = {
    "Подсолнечник": 90,
    "Томат": 60,
    "Морковь": 70,
    "Салат": 30,
    "Огурец": 50,
    "Редис": 25,
    "Петрушка": 80,
    "Укроп": 40
}

def calculate_plants():
    try:
        plant_name = plant_var.get()
        growth_days = plants_data[plant_name]

        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        target_date = datetime(year, month, day)
        now = datetime.now()

        if target_date <= now:
            result_label.config(text="Ошибка: выберите будущую дату!", fg="red")
            canvas.delete("all")
            return

        diff = target_date - now
        total_days = diff.days

        if total_days <= 0:
            result_label.config(text="Ошибка: дата должна быть в будущем!", fg="red")
            canvas.delete("all")
            return

        full_cycles = total_days // growth_days
        remaining_days = total_days % growth_days

        if full_cycles > 0:
            result_text = f"За выбранный период вырастет {full_cycles} полный(ых) цикл(ов) {plant_name}."
            if remaining_days > 0:
                result_text += f"\nЕщё {remaining_days} дней — неполный цикл."
        else:
            result_text = f"{plant_name} не успеет вырасти за выбранный период.\nОсталось {remaining_days} дней до первого урожая."

        result_label.config(text=result_text, fg="black")

        draw_plants(full_cycles, remaining_days, plant_name)

    except ValueError:
        result_label.config(text="Ошибка: введите корректные числа!", fg="red")
        canvas.delete("all")

def draw_plants(full_cycles, remaining_days, plant_name):
    canvas.delete("all")
    canvas_width = 300
    canvas_height = 150

    if full_cycles == 0 and remaining_days == 0:
        canvas.create_text(canvas_width//2, canvas_height//2,
                          text="Нет данных для отображения", fill="gray")
        return

    max_plants = min(full_cycles, 10)
    plant_width = canvas_width // (max_plants + 1)

    for i in range(max_plants):
        x = (i + 1) * plant_width
        canvas.create_line(x, canvas_height - 20, x, canvas_height - 80, width=2, fill="green")
        if "Подсолнечник" in plant_name:
            canvas.create_oval(x-15, canvas_height-90, x+15, canvas_height-60, fill="yellow", outline="orange")
        elif "Томат" in plant_name:
            canvas.create_oval(x-10, canvas_height-85, x+10, canvas_height-65, fill="red", outline="darkred")
        elif "Морковь" in plant_name:
            canvas.create_polygon(x, canvas_height-80, x-10, canvas_height-100, x+10, canvas_height-100, fill="orange", outline="darkorange")
            canvas.create_rectangle(x-3, canvas_height-20, x+3, canvas_height-80, fill="green", outline="darkgreen")
        else:
            canvas.create_oval(x-12, canvas_height-85, x+12, canvas_height-65, fill="lightgreen", outline="green")

    if remaining_days > 0 and full_cycles < 10:
        x = (full_cycles + 1) * plant_width
        progress = remaining_days / plants_data[plant_name]
        height = 20 + (60 * progress)
        canvas.create_line(x, canvas_height - 20, x, canvas_height - 20 - height, width=2, fill="green")
        canvas.create_oval(x-8, canvas_height-30-height, x+8, canvas_height-10-height, fill="lightblue", outline="blue")

root = tk.Tk()
root.title("Симулятор роста растений")
root.geometry("450x500")

title_label = tk.Label(root, text="Симулятор роста растений", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

plant_label = tk.Label(root, text="Выберите растение:")
plant_label.pack()

plant_var = tk.StringVar(value="Подсолнечник")
plant_combo = ttk.Combobox(root, textvariable=plant_var, values=list(plants_data.keys()), state="readonly")
plant_combo.pack(pady=5)

date_frame = tk.Frame(root)
date_frame.pack(pady=10)

tk.Label(date_frame, text="День:").grid(row=0, column=0, padx=5)
day_entry = tk.Entry(date_frame, width=5)
day_entry.grid(row=0, column=1, padx=5)

tk.Label(date_frame, text="Месяц:").grid(row=0, column=2, padx=5)
month_entry = tk.Entry(date_frame, width=5)
month_entry.grid(row=0, column=3, padx=5)

tk.Label(date_frame, text="Год:").grid(row=0, column=4, padx=5)
year_entry = tk.Entry(date_frame, width=8)
year_entry.grid(row=0, column=5, padx=5)

calculate_button = tk.Button(root, text="Рассчитать рост растений", command=calculate_plants)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 10), justify="left", anchor="w")
result_label.pack(pady=10)

canvas = tk.Canvas(root, width=300, height=150, bg="white", relief="solid", bd=1)
canvas.pack(pady=10)

info_label = tk.Label(root, text="Визуализация роста растений (максимум 10 растений)", font=("Arial", 8), fg="gray")
info_label.pack()

now = datetime.now()
day_entry.insert(0, str(now.day))
month_entry.insert(0, str(now.month))
year_entry.insert(0, str(now.year))

root.mainloop()