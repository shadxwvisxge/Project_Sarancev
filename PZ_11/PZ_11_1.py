#Дана последовательность целых чисел. Поменять местами ее первую и последнюю трети.
# Исходная последовательность
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Длина последовательности
n = len(sequence)

# Определяем границы третей
third = n // 3

# Вырезаем части последовательности
first_third = sequence[:third]
middle_part = sequence[third: n - third]
last_third = sequence[n - third:]

# Меняем местами первую и последнюю треть
result = last_third + middle_part + first_third

print("Исходная последовательность:", sequence)
print("Измененная последовательность:", result)