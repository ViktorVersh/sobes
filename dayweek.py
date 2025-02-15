import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
df = pd.read_csv('Аналитик — тестовое задание - data.csv')

# Вывод первых строк данных для проверки
print(df.head())

# Преобразование столбца с датой в формат datetime
df['event_date'] = pd.to_datetime(df['event_date'])

# Извлечение дня недели и создание нового столбца
df['day_of_week'] = df['event_date'].dt.day_name()

# Группировка по дням недели и подсчёт количества событий
events_by_day = df['day_of_week'].value_counts()

# Сортировка по дням недели (понедельник - воскресенье)
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
events_by_day = events_by_day.reindex(days_order)

# Построение графика
events_by_day.plot(kind='bar', title='Количество посещений занятий по дням недели', color='green')

# Настройка графика
plt.xlabel('День недели')
plt.ylabel('Количество посещений')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
