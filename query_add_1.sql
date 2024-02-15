--Середній бал, який певний викладач ставить певному студентові.

SELECT AVG(g.grade) AS average_grade
FROM grades g
JOIN subjects sub ON g.subject_id = sub.id
JOIN teachers t ON sub.teacher_id = t.id
JOIN students s ON g.student_id = s.id
WHERE t.name = 'Michele Evans' AND s.name = 'Kathleen Clark';