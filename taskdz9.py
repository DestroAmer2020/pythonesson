import pandas as pd
import matplotlib.pyplot as plt
# Завантаження даних
equipment_losses = pd.read_csv('russia_losses_equipment.csv')
equipment_correction = pd.read_csv('russia_losses_equipment_correction.csv')
personnel_losses = pd.read_csv('russia_losses_personnel.csv')
# Попередня обробка даних
equipment_losses = equipment_losses.dropna().drop_duplicates()
equipment_correction = equipment_correction.dropna().drop_duplicates()
personnel_losses = personnel_losses.dropna().drop_duplicates()
# Аналіз даних
equipment_stats = equipment_losses.describe()
correction_stats = equipment_correction.describe()
personnel_stats = personnel_losses.describe()
# Групування для аналізу підгруп
equipment_grouped = equipment_losses.groupby('Year').sum()
# Відсортування даних
sorted_equipment = equipment_losses.sort_values(by='EquipmentLosses', ascending=False)
# Візуалізація даних
plt.figure(figsize=(10, 6))
plt.plot(equipment_grouped.index, equipment_grouped['EquipmentLosses'], marker='o')
plt.title('Кількість втрат техніки по роках')
plt.xlabel('Рік')
plt.ylabel('Кількість втрат')
plt.grid(True)
plt.show()