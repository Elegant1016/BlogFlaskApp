import sqlite3

with sqlite3.connect('new.db') as conn:
    cursor = conn.cursor()
    query = "SELECT city, state FROM population"
    for row in cursor.execute(query):
        print(row[0], row[1])
