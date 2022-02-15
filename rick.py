import sqlite3 as sq

with sq.connect("rick.db") as con:
    cur = con.cursor()

    # cur.execute("DROP TABLE IF EXISTS famely") # чтоб пересоздать таблицу famely
    cur.execute("""CREATE TABLE IF NOT EXISTS famely(
    famely_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sex TEXT,
    old INTEGER
    )""")

    cur.execute("SELECT * FROM famely")
    if len(cur.fetchall()) == 0:
        print('создаем таблицу famaly')
        data = [('Катя', 'Ж', 46), ('Паша', 'М', 46), ('Андрей', 'М', 25), ('Тимофей', 'М', 12),
                ('Миша', 'М', 9), ('Настя', 'Ж', 25), ('Маша', 'Ж', 1), ('Валентина', 'Ж', 70)]
        #for s in data:
            #cur.execute("INSERT INTO famely(name, sex, old) VALUES(?, ?, ?)", s)
            #cur.execute("INSERT INTO famely VALUES(NULL, ?, ?, ?)", s) # можно и так
        cur.executemany("INSERT INTO famely VALUES(NULL, ?, ?, ?)", data) # а можно и сразу так
        cur.execute("UPDATE famely SET sex = ? WHERE sex = 'Ж'", 'ж')
        cur.execute("UPDATE famely SET sex = :Sex WHERE sex LIKE 'М'", {'Sex' : 'м'})

    cur.execute("SELECT * FROM famely")
    for s in cur.fetchall():
        print(s)
    print()

    print('все женщины: ', end='')
    cur.execute("SELECT name FROM famely WHERE sex = 'ж'")
    for s in cur.fetchall():
        print(s[0], end=' ')
    print()
    print(' все мужики: ', end='')
    cur.execute("SELECT name FROM famely WHERE sex = 'м'")
    for s in cur.fetchall():
        print(s[0], end=' ')
