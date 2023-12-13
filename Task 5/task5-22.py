import csv
from collections import defaultdict
with open(database_file, mode='r') as file:
    reader = csv.DictReader(file)
    brand_years = defaultdict(list)
    for row in reader:
        brand_years[row["Марка"]].append(int(row["Рік"]))
    print("\nСтатистика:")
    for brand, years in brand_years.items():
        average_year = sum(years) / len(years)
        print(f"Середній рік випуску для {brand}: {average_year:.2f}")