-- Отримати оцінки студентів у вказаній групі з певного предмета на останньому занятті

SELECT students.name AS student_name, grades.grade, grades.date
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN students ON grades.student_id = students.id
JOIN groups ON subjects.group_id = groups.id
WHERE subjects.name = 'Further education lecturer' AND groups.number = 1
AND grades.date = (SELECT MAX(date) FROM grades WHERE subject_id = subjects.id);