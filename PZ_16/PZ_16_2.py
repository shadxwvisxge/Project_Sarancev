#Создайте класс "Автомобиль", который содержит информацию о марке, модели и
#годе выпуска. Создайте класс "Грузовик", который наследуется от класса
#"Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
#"Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
#информацию о количестве пассажиров.

# Базовый класс "Автомобиль"
class Avtomobil:
    def __init__(self, marka, model, year):
        self.marka = marka
        self.model = model
        self.year = year

    def show_info(self):
        print(f"Марка: {self.marka}, Модель: {self.model}, Год выпуска: {self.year}")

# Наследуемый класс "Грузовик" с грузоподъемностью
class Gruzovik(Avtomobil):
    def __init__(self, marka, model, year, gruzo_podъемnost):
        super().__init__(marka, model, year)
        self.gruzo_podъемnost = gruzo_podъемnost

    def show_info(self):
        super().show_info()
print(f"Грузоподъемность: кг")

# Наследуемый класс "Легковой автомобиль" с количеством пассажиров
class LegkovoyAvtomobil(Avtomobil):
    def __init__(self, marka, model, year, passagers):
        super().__init__(marka, model, year)
        self.passagers = passagers

    def show_info(self):
        super().show_info()
        print(f"Количество пассажиров: {self.passagers}")

# Примеры использования

# Создаем легковой автомобиль
legk = LegkovoyAvtomobil("BMW", "X5", 2022, 5)
legk.show_info()

print()

# Создаем грузовик
gruz = Gruzovik("KAMAZ", "Next", 2020, 15000)
gruz.show_info()