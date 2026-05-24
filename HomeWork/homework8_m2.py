
import sqlite3

connection = sqlite3.connect("cinema.db")
cursor = connection.cursor()

# Таблица пользователей
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
""")

# Таблица фильмов
cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        genre TEXT
    )
""")

# Таблица отзывов (связующая)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        movie_id INTEGER,
        rating INTEGER
    )
""")

connection.commit()
print("Таблицы созданы")

cursor.execute("INSERT INTO users (name) VALUES (?)", ("Анна",))
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Борис",))
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Виктор",))
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Галина",))
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Дмитрий",))

connection.commit()
print("Пользователи добавлены")

cursor.execute("INSERT INTO movies (title, genre) VALUES (?, ?)", ("Начало", "Фантастика"))
cursor.execute("INSERT INTO movies (title, genre) VALUES (?, ?)", ("Титаник", "Драма"))
cursor.execute("INSERT INTO movies (title, genre) VALUES (?, ?)", ("Интерстеллар", "Фантастика"))
cursor.execute("INSERT INTO movies (title, genre) VALUES (?, ?)", ("Джокер", "Триллер"))
cursor.execute("INSERT INTO movies (title, genre) VALUES (?, ?)", ("Аватар", "Фантастика"))

connection.commit()
print("Фильмы добавлены")

cursor.execute("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)", (1, 1, 9))
cursor.execute("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)", (1, 3, 10))
cursor.execute("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)", (2, 1, 8))
cursor.execute("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)", (2, 2, 7))
cursor.execute("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)", (3, 4, 6))
cursor.execute("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)", (3, 1, 9))
cursor.execute("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)", (4, 2, 8))
cursor.execute("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)", (4, 3, 7))
cursor.execute("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)", (5, 4, 10))
cursor.execute("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)", (5, 1, 8))

connection.commit()
print("Отзывы добавлены")

print("\n--- Все отзывы ---")
cursor.execute("""
    SELECT users.name, movies.title, reviews.rating
    FROM reviews
    JOIN users ON reviews.user_id = users.id
    JOIN movies ON reviews.movie_id = movies.id
""")

results = cursor.fetchall()
for row in results:
    print(f"{row[0]} | {row[1]} | Оценка: {row[2]}")

print("\n--- Все фильмы (даже без отзывов) ---")
cursor.execute("""
    SELECT movies.title, reviews.rating
    FROM movies
    LEFT JOIN reviews ON movies.id = reviews.movie_id
""")

results = cursor.fetchall()
for row in results:
    if row[1] is None:
        print(f"{row[0]} | Нет отзывов")
    else:
        print(f"{row[0]} | Оценка: {row[1]}")

print("\n--- Агрегации ---")

cursor.execute("SELECT AVG(rating) FROM reviews")
avg_rating = cursor.fetchone()[0]
print(f"Средняя оценка: {round(avg_rating, 2)}")

cursor.execute("SELECT MAX(rating) FROM reviews")
max_rating = cursor.fetchone()[0]
print(f"Максимальная оценка: {max_rating}")

cursor.execute("SELECT MIN(rating) FROM reviews")
min_rating = cursor.fetchone()[0]
print(f"Минимальная оценка: {min_rating}")