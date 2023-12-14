from datetime import datetime

class City:
    def init(self, name, interests):
        self.name = name
        self.interests = interests
        self.stay_dates = {}
        self.budget = 0
    def add_stay_dates(self, start_date, end_date):
        self.stay_dates = {"start_date": start_date, "end_date": end_date}
    def set_budget(self, budget):
        self.budget = budget

class TripPlanner:
    def init(self):
        self.cities = []
    def add_city(self, name, interests):
        city = City(name, interests)
        self.cities.append(city)
    def plan_trip(self):
        for city in self.cities:
            print(f"\nМісто: {city.name}")
            print(f"Інтереси: {', '.join(city.interests)}")
            print(f"Дата перебування: {city.stay_dates['start_date']} - {city.stay_dates['end_date']}")
            print(f"Бюджет: {city.budget}")

planner = TripPlanner()

planner.add_city("Київ", ["історія", "мистецтво"])
planner.cities[0].add_stay_dates(datetime(2023, 1, 1), datetime(2023, 1, 5))
planner.cities[0].set_budget(1000)

planner.add_city("Львів", ["архітектура", "гастрономія"])
planner.cities[1].add_stay_dates(datetime(2023, 1, 6), datetime(2023, 1, 8))
planner.cities[1].set_budget(800)

planner.add_city("Одеса", ["море", "культура"])
planner.cities[2].add_stay_dates(datetime(2023, 1, 9), datetime(2023, 1, 12))
planner.cities[2].set_budget(1200)

planner.add_city("Карпати", ["гори", "ліси"])
planner.cities[3].add_stay_dates(datetime(2023, 1, 1), datetime(2023, 1, 5))
planner.cities[3].set_budget(700)

planner.add_city("Волинь", ["замки", "заповідники"])
planner.cities[4].add_stay_dates(datetime(2023, 1, 6), datetime(2023, 1, 8))
planner.cities[4].set_budget(800)

planner.add_city("Івано-Франківськ", ["музеї", "ресторани"])
planner.cities[5].add_stay_dates(datetime(2023, 1, 9), datetime(2023, 1, 12))
planner.cities[5].set_budget(2200)

planner.plan_trip()