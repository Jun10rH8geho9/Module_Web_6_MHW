-- Знайти список студентів у певній групі

SELECT students.name
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN groups ON subjects.group_id = groups.id
WHERE groups.id = 1;