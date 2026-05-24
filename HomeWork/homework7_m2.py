
import sqlite3

connection = sqlite3.connect("store.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        quantity INTEGER
    )
""")

connection.commit()

def create_product(name, price, quantity):
    cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity))
    connection.commit()
    print(f"Товар '{name}' добавлен")

def read_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    for product in products:
        print(product)

def update_product(id, price):
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (price, id))
    connection.commit()
    print(f"Цена товара с id={id} обновлена на {price}")

def delete_product(id):
    cursor.execute("DELETE FROM products WHERE id = ?", (id,))
    connection.commit()
    print(f"Товар с id={id} удалён")

create_product("Хлеб", 50, 10)
create_product("Молоко", 80, 5)
create_product("Сыр", 250, 3)

print("\n--- Все товары ---")
read_products()
update_product(1, 55)
print("\n--- После обновления ---")
read_products()
delete_product(2)
print("\n--- После удаления ---")
read_products()