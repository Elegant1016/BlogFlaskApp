import sqlite3

with sqlite3.connect('new.db') as conn:
    cursor = conn.cursor()
    query = "SELECT population.city, population.population, regions.region FROM population, regions WHERE population.city = regions.city"
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
    except sqlite3.OperationalError:
        print("Error")
