-- Отримати оцінки студентів у вказаній групі з певного предмета на останньому занятті

SELECT s.name AS student_name, g.grade
FROM students s
JOIN groups gr ON s.group_id = gr.id
JOIN subjects sub ON gr.id = sub.group_id
JOIN grades g ON s.id = g.student_id AND sub.id = g.subject_id
WHERE gr.number = 2 AND sub.name = 'Public affairs consultant'
ORDER BY g.date DESC
LIMIT 1;