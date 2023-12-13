import csv
from operator import itemgetter

# Завдання 1: Створення бази даних
header = ["Ім'я", "Прізвище", "Вік", "Спеціальність"]

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)

# Завдання 2: Додавання записів
students_data = [
    ["Іван", "Іванов", 22, "Інформатика"],
    ["Марія", "Петрова", 19, "Математика"],
    ["Олександр", "Сидоров", 21, "Фізика"],
    ["Анна", "Коваленко", 23, "Хімія"],
    ["Петро", "Семененко", 20, "Історія"]
]

with open('students.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(students_data)

# Завдання 3: Читання бази даних
with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Завдання 4: Пошук студентів старших 20 років
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row['Вік']) > 20:
            print(row)

# Завдання 5: Оновлення записів
with open('students.csv', 'r') as file:
    data = list(csv.reader(file))
    for student in data:
        if student[0] == "Олександр" and student[1] == "Сидоров":
            student[3] = "Економіка"

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Завдання 6: Видалення запису
with open('students.csv', 'r') as file:
    data = list(csv.reader(file))
    data = [student for student in data if not (student[0] == "Анна" and student[1] == "Коваленко")]

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Завдання 7: Сортування бази даних за віком
with open('students.csv', 'r') as file:
    data = list(csv.reader(file))
    data.sort(key=itemgetter(2))  # Сортування за третім елементом (віком)

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Додаткове завдання: Статистика
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    stats = {}
    counts = {}

    for row in reader:
        specialty = row['Спеціальність']
        age = int(row['Вік'])

        if specialty not in stats:
            stats[specialty] = age
            counts[specialty] = 1
        else:
            stats[specialty] += age
            counts[specialty] += 1

    for specialty, total_age in stats.items():
        average_age = total_age / counts[specialty]
        print(f"Спеціальність: {specialty}, Середній вік: {average_age}")