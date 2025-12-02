import requests
import sqlite3

conn = sqlite3.connect("cats.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS facts (id INTEGER PRIMARY KEY AUTOINCREMENT, fact TEXT, length INT)")
conn.commit()

max_len = input("Число: ")

url = "https://catfact.ninja/fact?max_length=" + max_len
resp = requests.get(url).json()

fact = resp["fact"]
length = resp["length"]

print("\nAPI:")
print(fact)

cur.execute("INSERT INTO facts(fact, length) VALUES (?, ?)", (fact, length))
conn.commit()

print("\nзбережено у базу")

show = input("Показати всі записи? (y/n): ")

if show.lower() == "y":
    cur.execute("SELECT * FROM facts")
    data = cur.fetchall()
    print("\nДані у базі:")
    for d in data:
        print("ID:", d[0])
        print("Факт:", d[1])
        print("Довжина:", d[2], "\n")

conn.close()
