#Задача из пз 4_2
import tkinter as tk
from tkinter import messagebox

def check_power_of_three():
    try:
        N = int(entry.get())
        if N <= 0:
            messagebox.showerror("Ошибка", "Введите целое число больше 0")
            return
        # Проверка, является ли N степенью 3
        # Алгоритм: если N == 3^k, то логарифм N по основанию 3 целый
        # или можно последовательно делить N на 3, пока не получим 1.
        temp = N
        while temp > 1:
            if temp % 3 != 0:
                result_label.config(text="FALSE")
                return
            temp //= 3
        # Если цикл прошел, значит N — степень 3
        result_label.config(text="TRUE")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целое число")

# Создаем окно
root = tk.Tk()
root.title("Проверка степени числа 3")

# Метка и поле ввода для числа N
label = tk.Label(root, text="Введите целое число N (>0):")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

# Кнопка для проверки
check_button = tk.Button(root, text="Проверить", command=check_power_of_three)
check_button.pack(pady=5)

# Метка для вывода результата
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Запуск главного цикла
root.mainloop()