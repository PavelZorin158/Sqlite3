import sqlite3 as sq

with sq.connect("users.db") as con:
    cur = con.cursor()

#    cur.execute("DROP TABLE IF EXISTS users")
#    cur.execute("""CREATE TABLE IF NOT EXISTS users(
#    user_id INTEGER PRIMARY KEY,
#    name TEXT NOT NULL,
#    sex INTEGER NOT NULL DEFAULT 1,
#    old INTEGER,
#    score INTEGER
#    )""")

    cur.execute("SELECT * FROM users ORDER BY old")
    result = cur.fetchall()
    for i in result:
        print(i)
