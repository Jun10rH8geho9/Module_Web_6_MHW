import sqlite3
from faker import Faker

fake = Faker()

# Генерація даних для студентів
fake_students = [(fake.name(), fake.date_of_birth()) for _ in range(50)]

# Генерація даних для груп
fake_groups = [(fake.random_int(1, 5)) for _ in range(3)]

# Генерація даних для викладачів
fake_teachers = [(fake.name()) for _ in range(5)]

# Генерація даних для предметів
fake_subjects = [(fake.random_element(fake_teachers), fake.job(), fake.random_element(fake_groups)) for _ in range(8)]

# Генерація даних для оцінок студентів
fake_grades = [(fake.random_element(fake_students), fake.random_element(fake_subjects), fake.random_int(1, 100), fake.date_time_this_year()) for _ in range(20)]

# Підключення до бази даних
conn = sqlite3.connect('fake_university.db')
cursor = conn.cursor()

# Створення таблиць, якщо вони не існують
cursor.execute('''CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY, name TEXT, dob DATE)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS groups
             (id INTEGER PRIMARY KEY, number INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS teachers
             (id INTEGER PRIMARY KEY, name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS subjects
             (id INTEGER PRIMARY KEY, teacher_id INTEGER, name TEXT, group_id INTEGER,
              FOREIGN KEY(teacher_id) REFERENCES teachers(id),
              FOREIGN KEY(group_id) REFERENCES groups(id))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS grades
             (student_id INTEGER, subject_id INTEGER, grade INTEGER, date DATETIME,
              FOREIGN KEY(student_id) REFERENCES students(id),
              FOREIGN KEY(subject_id) REFERENCES subjects(id))''')

# Вставка даних
cursor.executemany('INSERT INTO students (name, dob) VALUES (?, ?)', [(name, str(dob)) for name, dob in fake_students])
cursor.executemany('INSERT INTO groups (number) VALUES (?)', [(g,) for g in fake_groups])
cursor.executemany('INSERT INTO teachers (name) VALUES (?)', [(t,) for t in fake_teachers])
cursor.executemany('INSERT INTO subjects (teacher_id, name, group_id) VALUES (?, ?, ?)', fake_subjects)

# Вставка даних для оцінок студентів
for grade in fake_grades:
    student_name, subject_info, grade_value, grade_date = grade
    student_name_only = student_name[0]  # Extracting only the name from the tuple
    # Отримання id студента за ім'ям
    cursor.execute('SELECT id FROM students WHERE name = ?', (student_name_only,))
    result = cursor.fetchone()
    if result:
        student_id = result[0]
        # Отримання id предмету за інформацією про предмет
        teacher_name, subject_name, group_number = subject_info
        cursor.execute('SELECT id FROM subjects WHERE name = ? AND group_id = (SELECT id FROM groups WHERE number = ?) AND teacher_id = (SELECT id FROM teachers WHERE name = ?)', (subject_name, group_number, teacher_name))
        result = cursor.fetchone()
        if result:
            subject_id = result[0]
            # Вставка оцінки
            cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)', (student_id, subject_id, grade_value, grade_date))

# Збереження змін
conn.commit()

# Закриття з'єднання з базою даних
conn.close()