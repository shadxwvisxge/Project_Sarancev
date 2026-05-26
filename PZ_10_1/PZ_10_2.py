#Из предложенного текстового файла (text18-25.txt) вывести на экран его содержимое,
#количество символов, принадлежащих к группе букв. Сформировать новый файл, в
#который поместить текст в стихотворной форме предварительно удалив букву «с» из текста.
import os

# Указываем имя файла
file_name = 'text18-25.txt'

# Проверяем, существует ли файл
if not os.path.exists(file_name):
    print(f"Ошибка: Файл '{file_name}' не найден. Пожалуйста, убедитесь, что файл загружен.")
else:
    try:
        # Открываем исходный файл для чтения в кодировке UTF-8
        # Если возникнет ошибка UnicodeDecodeError, попробуйте изменить 'utf-8' на 'utf-8-sig' или 'cp1251'
        # Например: with open(file_name, 'r', encoding='utf-8-sig') as file:
        with open(file_name, 'r', encoding='utf-16') as file:
            # Читаем все содержимое файла
            text = file.read()

        # Выводим содержимое файла на экран
        print("Содержимое файла:")
        print(text)

        # Подсчитываем количество букв в тексте
        # Используем str.isalpha(), чтобы проверить, является ли символ буквой
        letter_count = sum(1 for ch in text if ch.isalpha())

        # Выводим количество букв
        print(f"\nКоличество букв в тексте: {letter_count}")

        # Удаляем букву 'с' и 'С' из текста для стихотворной формы
        # Для этого используем метод .replace()
        text_without_s = text.replace('с', '').replace('С', '')

        # Записываем полученный текст в новый файл
        new_file_name = 'new_text.txt'
        with open(new_file_name, 'w', encoding='utf-16') as new_file:
            new_file.write(text_without_s)

        print(f"\nСоздан новый файл '{new_file_name}' без буквы 'с'.")

    except UnicodeDecodeError as e:
        print(f"Ошибка кодировки при чтении файла '{file_name}': {e}")
        print("Пожалуйста, попробуйте изменить кодировку на 'utf-8-sig' или 'cp1251' в строке открытия файла.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")