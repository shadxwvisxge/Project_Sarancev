#В матрице элементы второго столбца возвести в квадрат.

import random
#Размеры матрицы
rows, cols = 4, 4
#Генерируем случайную матрицу
matrix = [[random.randint(0, 10) for _ in range(cols)] for _ in range(rows)]
print("Исходная матрица:")
for row in matrix:
    print(row)
# Возводим элементы второго столбца в квадрат с помощью спискового включения
matrix = [
    [
        matrix[i][j] if j != 1 else matrix[i][j] ** 2
        for j in range(cols)
    ]
    for i in range(rows)
]
print("Обновленная матрица после возведения элементов второго столбца в квадрат:")
for row in matrix:
    print(row)