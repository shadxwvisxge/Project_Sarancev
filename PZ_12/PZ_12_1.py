#В матрице найти сумму элементов второй половины матрицы.

import random
# Размеры матрицы
rows, cols = 4, 4
# Генерируем случайную матрицу
matrix = [[random.randint(0, 10) for _ in range(cols)] for _ in range(rows)]
print("Исходная матрица:")
for row in matrix:
    print(row)
# Предположим, что "вторая половина" — нижняя половина
half = rows // 2
sum_vtoroy_chasti = sum(sum(row) for row in matrix[half:])
print("Сумма элементов второй половины матрицы:", sum_vtoroy_chasti)