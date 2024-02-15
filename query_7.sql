-- Знайти оцінки студентів у окремій групі з певного предмета.

SELECT s.name AS student_name, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
JOIN groups gr ON sub.group_id = gr.id
WHERE gr.number = 2 AND sub.name = 'Event organiser';