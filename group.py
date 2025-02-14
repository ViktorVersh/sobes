import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
df = pd.read_csv('Аналитик — тестовое задание - data.csv')

# Вывод первых строк данных для проверки
print(df.head())

# Группировка по группам и подсчёт количества посещений
attendance_by_learn = df.groupby('group_ids')['is_attend'].sum()

# Построение столбчатой диаграммы
attendance_by_learn.plot(kind='bar', title='Посещаемость по группам')

# Настройка графика
plt.xlabel('Группы')
plt.ylabel('Посещаемость')
plt.xticks(rotation=45)  # Поворот подписей для удобства чтения
plt.tight_layout()  # Автоматическая настройка layout
plt.grid(True)
plt.show()
