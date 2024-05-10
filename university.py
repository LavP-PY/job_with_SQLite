import sqlite3


class University():
    name = 'Urban'

    def __init__(self):
        self.connection = sqlite3.connect('students.db')
        self.cursor = self.connection.cursor()

    def add_student(self, name, age) -> None:
        self.cursor.execute("INSERT INTO Students (name, age) VALUES (?, ?)", (name, age))
        self.connection.commit()
        self.connection.close()

    def add_grade(self, student_id, subject, grade) -> None:
        self.cursor.execute("INSERT INTO Grades (student_id, subject, grade) VALUES (?, ?, ?)", (student_id, subject, grade))
        self.connection.commit()
        self.connection.close()

    def get_students(self, subject=None):
        if subject is not None:
            self.cursor.execute('SELECT Students.id, Students.name, Students.age, Grades.subject, Grades.grade '
                                'FROM Students INNER JOIN Grades ON Students.id=Grades.student_id '
                                'WHERE subject = ?', (subject,))
        else:
            self.cursor.execute('SELECT Students.id, Students.name, Students.age, Grades.subject, Grades.grade '
                                'FROM Students INNER JOIN Grades ON Students.id=Grades.student_id ')
        print(self.cursor.fetchall())
        self.connection.close()

    def update_age(self, name, age):
        self.cursor.execute('UPDATE Students SET age = ? WHERE name = ?', (age, name))
        self.connection.commit()
        self.connection.close()

    def update_name(self, id, name):
        self.cursor.execute('UPDATE Students SET name = ? WHERE id = ?', (name, id))
        self.connection.commit()
        self.connection.close()

    def update_grade(self, student_id, subject, grade):
        self.cursor.execute(f'UPDATE Grades SET grade = {grade} WHERE student_id = {student_id} subject = {subject}')
        self.cursor.execute('UPDATE Grades SET grade = ? WHERE student_id = ? subject = ?', (grade, student_id, subject))
        self.connection.commit()
        self.connection.close()

    def delete_str(self, id):
        self.cursor.execute('DELETE FROM Students WHERE id = ?', (id,))
        self.cursor.execute('DELETE FROM Grades WHERE student_id = ?', (id,))
        self.connection.commit()
        self.connection.close()
        pass


univer = University()
# univer.add_student('Jake', 24)
# univer.get_students()
# univer.add_grade(16, 'Python', 4.8)
# univer.add_grade(16, 'C++', 4.5)
# univer.get_students()
# univer.update_name(id=2, name='Олег Новых')
# univer.update_age(age=22, name='Олег Новых')
# univer.update_grade(student_id=2, subject='C++', grade=4.9)
# univer.get_students(subject='C++')
# univer.delete_str(16)
univer.get_students()
