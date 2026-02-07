# Определяем множества туров у каждого агентства
voyage = {"Мексика", "Канада", "Израиль", "Италия"}
reina_tour = {"Англия", "Япония", "Канада", "ЮАР"}

in_reina = voyage - reina_tour

in_voyage = reina_tour - voyage

obshie_tours = voyage & reina_tour

equal = voyage == reina_tour

# Вывод результатов
print("Туры из Вояж, отсутствующие в РейнаТур:", in_reina)
print("Туры из РейнаТур, отсутствующие в Вояж:", in_voyage)
print("Общие туры:", obshie_tours)
print("Все перечни туров равны?", "Да" if equal else "Нет")
