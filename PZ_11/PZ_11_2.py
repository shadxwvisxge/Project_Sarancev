#Создать генератор (yield), который выводит из строки только цифры.
#Создаём генератор
def digits_generator(s):
    for char in s:
        if char.isdigit():
            yield char

#Пример строки
text = "abc123xyz45"
#Выводим цифры из текста
for digit in digits_generator(text):
    print(digit)