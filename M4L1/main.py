import sqlite3
    
# Создаем подключение к базе данных
connection = sqlite3.connect('movie.db')

# Создание курсора для выполнения SQL-запросов
cursor = connection.cursor()

# Символ * обозначает все
cursor.execute("SELECT * FROM heroes")

# А можно выбирать только нужные поля (об этом поговорим подробнее на следующих уроках)
cursor.execute("SELECT name FROM heroes")

# Использование метода fetchall() для получения результатов
result = cursor.fetchall()

# Вывод результатов
for row in result:
    print(row)

# Закрываем соединение с базой данных после использования
connection.close()