import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
df = pd.read_csv('Аналитик — тестовое задание - data.csv')

# Вывод первых строк данных для проверки
print(df.head())

# Преобразование столбца с датой в формат datetime
df['event_date'] = pd.to_datetime(df['event_date'])

# Построим график количества посещений по датам
attendance_by_date = df.groupby('event_date')['is_attend'].sum()

# Построение графика
attendance_by_date.plot(kind='line', title='График посещений по датам')

# Настройка осей и отображение графика
plt.xlabel('Дата')
plt.ylabel('Количество посещений')
plt.xticks(rotation=45)  # Поворот подписей дат для удобства чтения
plt.tight_layout()  # Автоматическая настройка layout
plt.grid(True)
plt.show()
