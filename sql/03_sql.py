import sqlite3

# with helps in not writing the commit, close calls
with sqlite3.connect("new.db") as conn:
    cursor = conn.cursor()
    cities = [('Boston', 'MA', 23232),
              ('Chicago', 'IL', 34244),
              ('Houston', 'TX', 232353)
              ]

    cursor.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)
