-- Знайти середній бал у групах з певного предмета.

SELECT groups.number, AVG(grades.grade) AS average_grade
FROM groups
JOIN subjects ON groups.id = subjects.group_id
JOIN grades ON subjects.id = grades.subject_id
WHERE subjects.name = "Health physicist"
GROUP BY groups.number;