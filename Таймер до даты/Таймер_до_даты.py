import tkinter as tk
from datetime import datetime

def start_timer():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        target_date = datetime(year, month, day)
        now = datetime.now()

        if target_date <= now:
            result_label.config(text="Ошибка: выберите будущую дату!", fg="red")
            return

        diff = target_date - now
        days = diff.days
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        result_label.config(
            text=f"Осталось: {days} дней, {hours:02d}:{minutes:02d}:{seconds:02d}",
            fg="black"
        )

    except ValueError:
        result_label.config(text="Ошибка: введите корректные числа!", fg="red")

root = tk.Tk()
root.title("Сколько времени до даты?")
root.geometry("350x200")

tk.Label(root, text="День:").place(relx=0.3, rely=0.1, anchor="center")
day_entry = tk.Entry(root, width=10)
day_entry.place(relx=0.6, rely=0.1, anchor="center")

tk.Label(root, text="Месяц:").place(relx=0.3, rely=0.25, anchor="center")
month_entry = tk.Entry(root, width=10)
month_entry.place(relx=0.6, rely=0.25, anchor="center")

tk.Label(root, text="Год:").place(relx=0.3, rely=0.4, anchor="center")
year_entry = tk.Entry(root, width=10)
year_entry.place(relx=0.6, rely=0.4, anchor="center")

start_button = tk.Button(root, text="Проверить", command=start_timer)
start_button.place(relx=0.5, rely=0.55, anchor="center")

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.place(relx=0.5, rely=0.75, anchor="center")

root.mainloop()