import random
class CafeSimulation:
    def __init__(self, num_tables, num_waiters):
        self.num_tables = num_tables
        self.num_waiters = num_waiters
        self.tables = [False] * num_tables
        self.waiters = [False] * num_waiters
        self.customers = []
    def generate_customers(self, arrival_rate):
        num_customers = random.randint(0, 5)
        for _ in range(num_customers):
            self.customers.append(random.randint(1, 3))
    def simulate(self, sim_duration):
        for current_time in range(sim_duration):
            self.generate_customers(0.2)
            self.serve_customers(current_time)
        self.analyze_simulation()
    def serve_customers(self, current_time):
        for i, customer in enumerate(self.customers):
            if customer > 0:
                customer -= 1
            else:
                self.customers.pop(i)
                if False in self.tables:
                    free_table = self.tables.index(False)
                    self.tables[free_table] = True
                else:
                    print(f"No available tables at time {current_time}")
    def analyze_simulation(self):
        print(f"Tables: {self.tables}")
        print(f"Customers: {self.customers}")
        print(f"Waiters: {self.waiters}")
        
# Приклад використання
cafe = CafeSimulation(num_tables=3, num_waiters=2)
cafe.simulate(sim_duration=10)