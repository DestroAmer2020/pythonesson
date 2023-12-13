import csv
# 1. Створення бази даних
header = ["Марка", "Модель", "Рік", "Колір"]
database_file = "база_даних_автомобілів.csv"
with open(database_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
# 2. Додавання записів
data = [
    ["Toyota", "Camry", 2020, "Сірий"],
    ["Honda", "Civic", 2018, "Чорний"],
    ["Ford", "Mustang", 2022, "Червоний"],
    ["Chevrolet", "Malibu", 2019, "Синій"],
    ["Tesla", "Model 3", 2021, "Білий"]
]
with open(database_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
# 3. Читання бази даних
with open(database_file, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# 4. Пошук (optional)
with open(database_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["Рік"] == "2020":
            print(row)
# 5. Оновлення записів
with open(database_file, mode='r') as file:
    reader = csv.reader(file)
    rows = list(reader)
for i in range(1, len(rows)):
    if rows[i][0] == "Tesla" and rows[i][1] == "Model 3":
        rows[i][3] = "Чорний"
with open(database_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
# 6. Видалення запису
with open(database_file, mode='r') as file:
    reader = csv.reader(file)
    rows = list(reader)
index_to_delete = None
for i in range(1, len(rows)):
    if rows[i][0] == "Ford" and rows[i][1] == "Mustang":
        index_to_delete = i
if index_to_delete is not None:
    del rows[index_to_delete]
with open(database_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
# 7. Сортування бази даних (optional)
with open(database_file, mode='r') as file:
    reader = csv.DictReader(file)
    rows = sorted(reader, key=lambda x: int(x["Рік"]))
for row in rows:
    print(row)
