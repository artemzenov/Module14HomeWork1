import sqlite3


count_user = 10
step_update = 2
step_delete = 3
age_select = 60

connection = sqlite3.connect('not_telegram.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
'''
)

for i in range(1, count_user+1):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'User{i}', f'example{i}@gmail.com', 10*i, 1000))

for i in range(1, count_user+1, step_update):
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))

for i in range(1, count_user+1, step_delete):
    cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (age_select,))
result_select = cursor.fetchall()
for i_user in result_select:
    print(f'Имя: {i_user[0]} / Почта: {i_user[1]} / Возраст: {i_user[2]} / Баланс: {i_user[3]}')

connection.commit()
connection.close()