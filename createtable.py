import pandas as pd

# Загрузка данных из CSV-файла
csv_file = 'Аналитик — тестовое задание - data.csv'
df = pd.read_csv(csv_file)

# Название таблицы в базе данных
table_name = 'Attendance'

# Создание SQL-запросов для вставки данных
sql_queries = []
for index, row in df.iterrows():
    values = ", ".join([f"'{str(value)}'" for value in row.values])
    sql_query = f"INSERT INTO {table_name} VALUES ({values});"
    sql_queries.append(sql_query)

# Сохранение SQL-запросов в файл
sql_file = 'output.sql'
with open(sql_file, 'w', encoding='utf-8') as f:
    for query in sql_queries:
        f.write(query + '\n')

print(f"SQL-запросы сохранены в файл: {sql_file}")