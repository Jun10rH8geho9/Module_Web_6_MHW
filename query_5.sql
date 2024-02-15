--Знайти які курси читає певний викладач.

SELECT sub.name AS subject_name
FROM subjects sub
JOIN teachers t ON sub.teacher_id = t.id
WHERE t.name = 'Eric Robinson';