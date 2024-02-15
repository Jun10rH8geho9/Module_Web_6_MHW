import sqlite3
from faker import Faker
from datetime import datetime

def adapt_datetime(dt):
    # Перетворення об'єкта datetime в рядок у форматі, який розуміє sqlite3
    return dt.strftime('%d-%m-%Y %H:%M:%S')

# Реєстрація адаптера
sqlite3.register_adapter(datetime, adapt_datetime)

fake = Faker()

# Генерація даних для студентів
fake_students = [(fake.name(), fake.date_of_birth()) for _ in range(50)]

# Генерація даних для груп
fake_groups = [(fake.random_int(1, 5)) for _ in range(3)]

# Генерація даних для викладачів
fake_teachers = [(fake.name()) for _ in range(fake.random_int(3, 6))]

# Генерація даних для предметів
fake_subjects = [(fake.random_element(fake_teachers), fake.job(), fake.random_element(fake_groups)) for _ in range(8)]

# Генерація даних для оцінок студентів
fake_grades = [(fake.random_element(range(1, 51)), fake.random_element(range(1, 9)), fake.random_int(1, 100), fake.date_time_this_year()) for _ in range(20)]

# Підключення до бази даних
conn = sqlite3.connect('fake_university.db', detect_types=sqlite3.PARSE_DECLTYPES)
cursor = conn.cursor()

# Створення таблиць, якщо вони не існують
cursor.execute('''CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY, name TEXT, dob DATE)''')

# Генерація даних для студентів
fake_students = [(fake.name(), fake.date_of_birth()) for _ in range(50)]

# Вставка даних
cursor.executemany('INSERT INTO students (name, dob) VALUES (?, ?)', [(name, str(dob)) for name, dob in fake_students])

# Створення таблиць, якщо вони не існують
cursor.execute('''CREATE TABLE IF NOT EXISTS groups
             (id INTEGER PRIMARY KEY, number INTEGER)''')

# Генерація даних для груп
fake_groups = [(fake.random_int(1, 5)) for _ in range(3)]

# Вставка даних
cursor.executemany('INSERT INTO groups (number) VALUES (?)', [(g,) for g in fake_groups])

# Створення таблиць, якщо вони не існують
cursor.execute('''CREATE TABLE IF NOT EXISTS teachers
             (id INTEGER PRIMARY KEY, name TEXT)''')

# Генерація даних для викладачів
fake_teachers = [(fake.name()) for _ in range(5)]

# Вставка даних
cursor.executemany('INSERT INTO teachers (name) VALUES (?)', [(t,) for t in fake_teachers])

# Створення таблиць, якщо вони не існують
cursor.execute('''CREATE TABLE IF NOT EXISTS subjects
             (id INTEGER PRIMARY KEY, teacher_id INTEGER, name TEXT, group_id INTEGER,
              FOREIGN KEY(teacher_id) REFERENCES teachers(id),
              FOREIGN KEY(group_id) REFERENCES groups(id))''')

# Генерація даних для предметів
fake_subjects = [(fake.random_element(range(1, 6)), fake.job(), fake.random_element(range(1, 4))) for _ in range(8)]

# Вставка даних
cursor.executemany('INSERT INTO subjects (teacher_id, name, group_id) VALUES (?, ?, ?)', fake_subjects)

# Створення таблиць, якщо вони не існують
cursor.execute('''CREATE TABLE IF NOT EXISTS grades
             (student_id INTEGER, subject_id INTEGER, grade INTEGER, date DATETIME,
              FOREIGN KEY(student_id) REFERENCES students(id),
              FOREIGN KEY(subject_id) REFERENCES subjects(id))''')

# Генерація даних для оцінок студентів
fake_grades = [(fake.random_element(range(1, 31)), fake.random_element(range(1, 9)), fake.random_int(1, 100), fake.date_time_this_year()) for _ in range(20)]

# Вставка даних для оцінок студентів
for grade in fake_grades:
    student_id, subject_id, grade_value, grade_date = grade
    # Вставка оцінки
    cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)', (student_id, subject_id, grade_value, grade_date))

# Збереження змін
conn.commit()

# Закриття з'єднання з базою даних
conn.close()