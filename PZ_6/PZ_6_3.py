#Дано множество A из N точек (N > 2, точки заданы своими координатами x, у). Найти
#такую точку из данного множества, сумма расстояний от которой до остальных его
#точек минимальна, и саму эту сумму.
#Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
#R = √(x2 – x1)2 + (у2 – y1)2.
import math

# Ввод количества точек (больше 2)
N = int(input())

# Ввод координат точек: по одному на строку, разделённые пробелом
x_coords = []
y_coords = []
for _ in range(N):
    x, y = map(float, input().split())
    x_coords.append(x)
    y_coords.append(y)

# Вычисление расстояния между двумя точками
def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

min_sum = None
index_of_point = -1

# Для каждой точки считаем сумму расстояний до всех остальных
for i in range(N):
    total_distance = 0
    for j in range(N):
        if i != j:
            total_distance += dist(x_coords[i], y_coords[i], x_coords[j], y_coords[j])
    # Обновляем минимальную сумму и индекс точки
    if min_sum is None or total_distance < min_sum:
        min_sum = total_distance
        index_of_point = i

# Вывод результата: номер точки + 1 (чтобы было удобнее)
print(index_of_point + 1, min_sum)