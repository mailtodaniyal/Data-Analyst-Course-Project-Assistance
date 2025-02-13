import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("test_database.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS sales (
                    id INTEGER PRIMARY KEY,
                    product TEXT,
                    quantity INTEGER,
                    price REAL
                 )''')

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", [
    ("Laptop", 5, 1200),
    ("Phone", 10, 800),
    ("Tablet", 7, 600),
])

conn.commit()

df = pd.read_sql_query("SELECT * FROM sales", conn)

df["total_sales"] = df["quantity"] * df["price"]

plt.figure(figsize=(8, 5))
plt.bar(df["product"], df["total_sales"], color=['blue', 'green', 'red'])
plt.xlabel("Product")
plt.ylabel("Total Sales ($)")
plt.title("Sales Analysis")
plt.show()

conn.close()
