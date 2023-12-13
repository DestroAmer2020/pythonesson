import csv
from operator import itemgetter
# Завдання 1
header = ["Назва", "Автор", "Рік видання", "Жанр"]
with open('база_даних_книг.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
# Завдання 2
books_data = [
    ["Майстер і Маргарита", "Михайло Булгаков", 1966, "Фантастика"],
    ["1984", "Джордж Орвелл", 1949, "Дистопія"],
    ["Маленький принц", "Антуан де Сент-Екзюпері", 1943, "Пригоди"],
    ["Метро 2033", "Дмитро Глуховський", 2005, "Постапокаліптика"],
    ["Гра престолів", "Джордж Р. Р. Мартін", 1996, "Фентезі"]
]
with open('база_даних_книг.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(books_data)
# Завдання 3
with open('база_даних_книг.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# Завдання 4
search_year = 2000
with open('база_даних_книг.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row['Рік видання']) > search_year:
            print(row)
# Завдання 5
with open('база_даних_книг.csv', 'r') as file:
    data = list(csv.reader(file))
    for book in data:
        if book[0] == "Майстер і Маргарита":
            book[3] = "Класика"
with open('база_даних_книг.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
# Завдання 6
with open('база_даних_книг.csv', 'r') as file:
    data = list(csv.reader(file))
    data = [book for book in data if not (book[0] == "Метро 2033" and book[1] == "Дмитро Глуховський")]
with open('база_даних_книг.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
# Завдання 7
with open('база_даних_книг.csv', 'r') as file:
    data = list(csv.reader(file))
    data.sort(key=itemgetter(2))  # Сортування за третім елементом (ріком видання)
with open('база_даних_книг.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
# Додаткове завдання
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