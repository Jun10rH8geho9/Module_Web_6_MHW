-- Знайти оцінки студентів у окремій групі з певного предмета.

SELECT students.name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN groups ON subjects.group_id = groups.id
WHERE groups.id = 3 AND subjects.id = 3;