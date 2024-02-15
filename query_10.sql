--Список курсів, які певному студенту читає певний викладач.

SELECT subjects.name, students.name AS student_name, teachers.name AS teacher_name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.id = 3 AND teachers.id = 3