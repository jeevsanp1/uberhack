import sqlite3
conn = sqlite3.connect("main.db")
c=conn.cursor()
c.execute("""CREATE TABLE database (
    supplier real,
    location integer,
    services blob
    )""")
conn.commit()