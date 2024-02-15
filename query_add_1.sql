--Середній бал, який певний викладач ставить певному студентові.

SELECT teachers.name AS teacher_name, students.name AS student_name, AVG(grades.grade) AS average_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
JOIN students ON grades.student_id = students.id
WHERE teachers.id = 3 AND students.id = 3
GROUP BY teachers.name, students.name;