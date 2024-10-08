import sqlite3

conn = sqlite3.connect('example.db')

cur = conn.cursor()

cur.execute('''
        CREATE TABLE IF NOT EXISTS users
        (id INTEGER PRIMARY KEY ,
        name TEXT NOT NULL ,
        age INTEGER NOT NULL)
    ''')
conn.commit()

cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Алексей", 30))
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Игорь", 25))
conn.commit()
conn.close()