#https://www.digiseller.ru/preview/125077/p1_30116215520413.JPG
import tkinter as tk
from tkinter import ttk

# Создаем основное окно
root = tk.Tk()
root.title("Образец формы")
root.geometry("500x600")
root.configure(bg='white')

# Стиль для основных элементов
style = ttk.Style()
style.configure("TLabel", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10))
style.configure("Header.TLabel", font=("Arial", 14, "bold"))

# Заголовок
header = ttk.Label(root, text="Заголовок формы", style="Header.TLabel")
header.pack(pady=10)

# Основной рамочный блок
main_frame = ttk.Frame(root, padding=10, relief="groove", borderwidth=2)
main_frame.pack(fill='both', expand=True, padx=20)

# Добавим надписи и поля
# Первая строчка
label1 = ttk.Label(main_frame, text="Название организации:")
label1.grid(row=0, column=0, sticky='w')
entry1 = ttk.Entry(main_frame, width=50)
entry1.grid(row=0, column=1, padx=10, pady=5, sticky='w')

# Вторая строчка
label2 = ttk.Label(main_frame, text="Фамилия, имя, отчество сотрудника:")
label2.grid(row=1, column=0, sticky='w')
entry2 = ttk.Entry(main_frame, width=50)
entry2.grid(row=1, column=1, padx=10, pady=5, sticky='w')

# Третья строчка
label3 = ttk.Label(main_frame, text="Паспортные данные:")
label3.grid(row=2, column=0, sticky='w')
entry3 = ttk.Entry(main_frame, width=50)
entry3.grid(row=2, column=1, padx=10, pady=5, sticky='w')

# Четвертая строчка
label4 = ttk.Label(main_frame, text="Период работы в организации:")
label4.grid(row=3, column=0, sticky='w')
entry4 = ttk.Entry(main_frame, width=50)
entry4.grid(row=3, column=1, padx=10, pady=5, sticky='w')

# Пятая секция - Описание
label5 = ttk.Label(main_frame, text="(по желанию) Дополнительная информация:")
label5.grid(row=4, column=0, sticky='w')
text_frame = ttk.Frame(main_frame)
text_frame.grid(row=5, column=0, columnspan=2, padx=0, pady=5, sticky='we')

# Текстовое поле с прокруткой
text_box = tk.Text(text_frame, width=60, height=5, wrap='word', font=("Arial", 10))
scrollbar = ttk.Scrollbar(text_frame, orient='vertical', command=text_box.yview)
text_box['yscrollcommand'] = scrollbar.set

scrollbar.pack(side='right', fill='y')
text_box.pack(side='left', fill='both', expand=True)

# Верхняя линия разделителя
separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', pady=10, padx=20)

# Кнопки
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

btn_ok = ttk.Button(button_frame, text='OK')
btn_cancel = ttk.Button(button_frame, text='Отмена')

btn_ok.pack(side='left', padx=20)
btn_cancel.pack(side='left', padx=20)

# Запуск интерфейса
root.mainloop()