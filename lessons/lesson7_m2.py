
import sqlite3

# A4
connect = sqlite3.connect('users.db')
# Рука и Ручка
cursor = connect.cursor()


cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (50) NOT NULL,
            age INTEGER,
            hobby TEXT
        )
''')
connect.commit()



# CRUD  Create-Read-Update-Delete

def create_user(name, age, hobby):
    # cursor.execute(
    #     'INSERT INTO users(name, age, hobby) VALUES(?,?,?) ',
    #     (def_name, def_age, def_hobby)
    # )
    cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES("{name}", "{age}", "{hobby}")')
    connect.commit()
    print('пользователь добавлен!!')


# create_user("John Doe", 12, "Спать!!")
# create_user("Oleg", 12, "Спать!!")
# create_user("Ivan", 12, "Спать!!")
# create_user("Вася", 12, "Спать!!")

def read_all_user():
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchmany(3)
    print(data)

# read_all_user()

def update_user(name, rowid):
    cursor.execute(
        'UPDATE users SET name=? WHERE rowid =?',
        (name, rowid)
    )
    connect.commit()
    print('пользователь обнавлен!!')

# update_user("Oleg", 5)


def delete_user(rowid):
    cursor.execute(
        'DELETE FROM users WHERE rowid=?',
        (rowid,)
    )
    connect.commit()
    print('Пользователь удален!!')

delete_user(3)