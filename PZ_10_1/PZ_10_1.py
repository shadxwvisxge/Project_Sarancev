#Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Элементы первого и второго файлов:
#Элементы после сортировки:
#Количество элементов:
#Минимальный элемент кратный 2:
#Максимальный элемент кратный 5:

# Импортируем необходимые модули
import random


# Генерируем два файла с последовательностями чисел
def create_files():
    # Первое число: от 1 до 50
    # Второе число: от -50 до -1
    with open("file1.txt", "w", encoding="utf-8") as f1:
        numbers1 = [random.randint(1, 50) for _ in range(10)]
        f1.write(" ".join(map(str, numbers1)))

    with open("file2.txt", "w", encoding="utf-8") as f2:
        numbers2 = [random.randint(-50, -1) for _ in range(10)]
        f2.write(" ".join(map(str, numbers2)))


# Функция для чтения чисел из файла
def read_numbers(filename):
    with open(filename, "r", encoding="utf-8") as f:
        line = f.read()
        # Разделяем строку по пробелам и конвертируем в целые числа
        numbers = list(map(int, line.split()))
    return numbers


# Создаём файлы с числами
create_files()

# Читаем числа из файлов
nums1 = read_numbers("file1.txt")
nums2 = read_numbers("file2.txt")

# Обрабатываем и сортируем объединённый список
all_numbers = nums1 + nums2
sorted_numbers = sorted(all_numbers)

# Находим необходимые параметры
count_elements = len(sorted_numbers)
min_multiple_2 = min([num for num in sorted_numbers if num % 2 == 0], default="Нет элементов, кратных 2")
max_multiple_5 = max([num for num in sorted_numbers if num % 5 == 0], default="Нет элементов, кратных 5")

# Создаём итоговый файл
with open("result.txt", "w", encoding="utf-8") as result_file:
    result_file.write("Элементы первого и второго файлов:n")
    result_file.write(f"{nums1} {nums2}nn")
    result_file.write("Элементы после сортировки:n")
    result_file.write(f"{sorted_numbers}n")
    result_file.write(f"Количество элементов: {count_elements}n")
    result_file.write(f"Минимальный элемент кратный 2: {min_multiple_2}n")
    result_file.write(f"Максимальный элемент кратный 5: {max_multiple_5}n")