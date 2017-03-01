import sqlite3

with sqlite3.connect('new.db') as conn:
    cursor = conn.cursor()
    cursor.execute("DROP TABLE if exists regions")
    query = "CREATE TABLE regions (city TEXT, region TEXT)"
    cursor.execute(query)
    cities = [
            ('New York City', 'Northeast'),
            ('San Francisco', 'Southeast'),
            ('India', 'South'),
            ('Dallas', 'Central'),
            ('California', 'West'),
            ('Bangalore', 'Midwest')
            ]
    cursor.executemany("INSERT INTO regions VALUES(?, ?)", cities)
    cursor.execute("SELECT * FROM regions ORDER BY region ASC")

    rows = cursor.fetchall()

    for r in rows:
        print(r)
