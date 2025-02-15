import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
df = pd.read_csv('Аналитик — тестовое задание - data.csv')

# Вывод первых строк данных для проверки
print(df.head())

# Группировка по группам и подсчёт количества посещений
attendance_by_learn = df.groupby('group_ids')['is_attend'].sum()

# Создание фигуры с двумя подграфиками (1 строка, 2 столбца)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # 1 строка, 2 столбца, размер фигуры 12x5

# Построение столбчатой диаграммы на первом подграфике
attendance_by_learn.plot(kind='bar', ax=axes[0], title='Посещаемость по группам (столбчатая диаграмма)')
axes[0].set_xlabel('Группы')
axes[0].set_ylabel('Посещаемость')
axes[0].tick_params(axis='x', rotation=45)  # Поворот подписей оси X
axes[0].grid(True)

# Построение круговой диаграммы на втором подграфике
attendance_by_learn.plot(kind='pie', ax=axes[1], title='Посещаемость по группам (круговая диаграмма)', autopct='%1.1f%%')
axes[1].set_ylabel('')  # Убираем подпись оси Y для круговой диаграммы

# Настройка общего layout
plt.tight_layout()  # Автоматическая настройка layout, чтобы графики не перекрывались
plt.show()