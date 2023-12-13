class TimeTraveler:
    def __init__(self):
        self.events = [(1903, "Перший пілотований політ братів Райт"),
                       (1969, "Аполлон-11 досягає Місяця"),
                       (2001, "Перший політ людини в космосі")]
        self.time_dict = dict(self.events)
        self.desired_years = {1903, 1969, 2001}
    def travel(self, year):
        try:
            print(f"В {year} році сталася подія: {self.time_dict[year]}")
        except KeyError:
            print(f"Вибачте, подія для року {year} відсутня у словнику часу.")
    def add_event(self, year, event):
        self.time_dict[year] = event
        self.desired_years.add(year)
        print(f"Подія в {year} році додана: {event}")
    def remove_event(self, year):
        try:
            event = self.time_dict.pop(year)
            self.desired_years.remove(year)
            print(f"Подія в {year} році видалена: {event}")
        except KeyError:
            print(f"Вибачте, подія для року {year} відсутня у словнику часу.")

# Створення об'єкту мандрівника у часі
time_traveler = TimeTraveler()

# Приклад використання: подорож до року 1969
time_traveler.travel(1969)

# Додавання нової події у рік 2022
time_traveler.add_event(2022, "Запуск перших космічних туристів")

# Приклад видалення події за роком 1903
time_traveler.remove_event(1903)

# Подорож до року 1980 (рік відсутній у словнику часу)
time_traveler.travel(1980)