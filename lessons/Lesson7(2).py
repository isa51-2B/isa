import sqlite3

# A4
connect = sqlite3.connect('User.db')

# Рука с Ручкой
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR (40) NOT NULL,age INTEGER NOT NULL,hobby TEXT)''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS grades (grade_id INTEGER PRIMARI KEY AUTOINCREMENT, subject VARCHAR (50) NOT NULL,grade INTEGER NOT NULL,FOREING KEY (user_id) REFERENCES users(user_id))''')

def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")


name = input("Введите имя")
age = input("Введите возраст")
hobby = input("Введите Хоби")

add_user("user1", 23, "плавать")
add_user("user2", 23, "плавать")
add_user("user3", 23, "плавать")
add_user("user4", 23, "плавать")
add_user("user5", 23, "плавать")
