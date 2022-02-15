	conn - у нас будет объект соединения с базой
	conn = sqlite3.connect(r'ПУТЬ-К-ПАПКИ/orders.db') - Если файл уже существует, то функция connect осуществит подключение к нему.
	conn = sqlite3.connect(:memory:) - Создание базы в памяти
	cur = conn.cursor() - Создание объекта типа cursor. Он позволяет делать SQL-запросы к базе. Используем переменную cur для хранения объекта.
	cur.execute("ВАШ-SQL-ЗАПРОС-ЗДЕСЬ;") - Выполнение SQL запросов
	conn.commit() - сохраняет изменения для объекта conn


	
	cur.execute("""CREATE TABLE IF NOT EXISTS users(
	   userid INT PRIMARY KEY,
	   fname TEXT,
	   lname TEXT,
	   gender TEXT);
	""")
	conn.commit()
   
   В коде выше выполняются следующие операции:
Функция execute отвечает за SQL-запрос
SQL генерирует таблицу users
IF NOT EXISTS поможет при попытке повторного подключения к базе данных. Запрос проверит, существует ли таблица. Если да — проверит, ничего ли не поменялось.
Создаем первые четыре колонки: userid, fname, lname и gender. Userid — это основной ключ.
Сохраняем изменения с помощью функции commit для объекта соединения.



   В Python часто приходится иметь дело с переменными, в которых хранятся значения. Например, это может быть кортеж с информацией о пользователе.

	user = ('00002', 'Lois', 'Lane', 'Female')

   Если его нужно загрузить в базу данных, тогда подойдет следующий формат:

	cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
	conn.commit()



   Однако в переменной может быть и список с набором кортежей. Таким образом можно добавить несколько пользователей:

	more_users = [('00003', 'Peter', 'Parker', 'Male'), ('00004', 'Bruce', 'Wayne', 'male')]

   Но нужно использовать функцию executemany вместо обычной execute:

	cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", more_users)
	conn.commit()



	cur.execute("SELECT * FROM users;")
	one_result = cur.fetchone()
	print(one_result)
   Она вернет следующее:
	[(1, 'Alex', 'Smith', 'male')]

	cur.execute("SELECT * FROM users;")
	three_results = cur.fetchmany(3)
	print(three_results)
   Он вернет следующее:
	[(1, 'Alex', 'Smith', 'male'), (2, 'Lois', 'Lane', 'Female'), (3, 'Peter', 'Parker', 'Male')]

   Для получения всех результатов:
	cur.execute("SELECT * FROM users;")
	all_results = cur.fetchall()
	print(all_results)

   Для нескольких запросов
	cur.executescript("""SELECT * FROM users
	INSERT INTO users(name) VALUES('Вася')
	""")

	
	last = cur.lastrowid - возвращает последний rowid
