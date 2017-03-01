import sqlite3

with sqlite3.connect('blog.db') as conn:
    cursor = conn.cursor()
    query = "CREATE TABLE posts (title TEXT, post TEXT)"
    cursor.execute(query)
    cursor.execute('INSERT INTO posts VALUES ("Good", "This is good blog")')
    cursor.execute('INSERT INTO posts VALUES ("Good", "This is good blog")')
    cursor.execute('INSERT INTO posts VALUES ("Good", "This is good blog")')
    cursor.execute('INSERT INTO posts VALUES ("Good", "This is good blog")')
