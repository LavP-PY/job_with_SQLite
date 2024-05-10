# Домашнее задание по теме "Базы данных. SQLife3."
# Цель задания:
#
# Научиться использовать функционал sqlite3 для работы с базами данных.
#
# Задание:
# Студентов Urban'а становиться всё больше с каждым месяцем (не может не радовать), поэтому вам было поручено создать
# базу данных для отслеживания их и вашего прогресса в обучении.
# Т.к. вести все записи через Excell и прописывать формулы наши кураторы устали (неправда :) ), нужно создать базу данных и автоматизировать работу с ней при помощи ООП.
#
# Техническое задание:
# Создайте базу данных students.db
# В базе данных должны существовать 2 таблицы: students и grades
# В таблице students должны присутствовать следующие поля: id, name, age
# В таблице grades должны присутствовать следующие поля: id, student_id, subject, grade
# Так же нужно создать класс University со следующими атрибутами и методами:
# name - имя университета
# add_student(name, age) - метод добавления студента.
# add_grade(sudent_id, subject, grade) - метод добавления оценки.
# get_students(subject=None) - метод для возврата списка студентов в формате [(Ivan, 26, Python, 4.8), (Ilya, 24, PHP, 4.3)], где subject, если не является None(по умолчанию) и если такой предмет существует, выводит студентов только по этому предмету.

# Описание полей:
# id - в обоих таблицах обязательно PRIMARY KEY
# name - STR
# age - INT
# subject - STR
# grade - FLOAT
# и самое интересное student_id - INT (или внешний ключ)
#
# Внешний ключ - это данное в поле указывающее на id в другой таблице,
# оно может быть реализовано следующей командой в SQL: FOREIGN KEY (student_id) REFERENCES students(id),
# при создании таблицы.
# При этом поле student_id - существует как INT.
#
# Пример работы кода:
#
# Код:
# u1 = University('Urban')
#
# u1.add_student('Ivan', 26) # id - 1
# u1.add_student('Ilya', 24) # id - 2
#
# u1.add_grade(1, 'Python', 4.8)
# u1.add_grade(2, 'PHP', 4.3)
#
# print(u1.get_students())
# print(u1.get_students('Python'))
#
# Консоль:
# [(Ivan, 26, Python, 4.8), (Ilya, 24, PHP, 4.3)]
# [(Ivan, 26, Python, 4.8)]
#
# Примечание:
# Перед отправкой полной версии БД на GitHub сделайте при помощи вашего класса University и соответствующих
# объектов минимум 8 записей, где у каждого студента будет минимум по 2 зачёт (значит студентов будет 4).
#
# Пришлите ссылку на репозиторий GitHub со следующими файлами:
# Файл базы данных с расширением .db
# Файл(-ы) с классом University и соответствующим(-и) объектами (на которых тестировали).
#
# Помните, что веткой по умолчанию (default) должна быть выбрана та, где находятся необходимые файлы.
#
# Успеха!


import sqlite3

# Создаем подключение к базе данных (файл my_database.db будет создан)
# connection = sqlite3.connect('students.db')
# connection.close()

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('students.db')
cursor = connection.cursor()

# Создаем таблицу Students
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students 
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')

# Создаем таблицу Grades
cursor.execute('''
CREATE TABLE IF NOT EXISTS Grades 
(
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject TEXT NOT NULL,
    grade REAL,
    FOREIGN KEY (student_id) REFERENCES students(id)
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()


