import sqlite3

conn = sqlite3.connect("new.db")
cursor = conn.cursor()
cursor.execute("INSERT INTO population VALUES('New York', 'NY', 77777)")
cursor.execute("INSERT INTO population VALUES('Bangalore', 'BLR', 33333)")
cursor.execute("INSERT INTO population VALUES('Sigma', 'SIG', 22222)")
cursor.execute("INSERT INTO population VALUES('Karnataka', 'KA', 21212)")
conn.commit()
conn.close()
