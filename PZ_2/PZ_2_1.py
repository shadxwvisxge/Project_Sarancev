try:
    N = int(input("Введите количество секунд"))
    if N < 0:
        print("Значение отрицательное")
    else:
        fullhours = N // 3600
        print(f"Прошло полных часов: {fullhours}")
except ValueError:
    print("Значение введено не корректно")