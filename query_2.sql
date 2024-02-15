-- Знайти студента із найвищим середнім балом з певного предмета.

SELECT students.name, AVG(grades.grade) AS average_grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.name = "Set designer"
GROUP BY students.id
ORDER BY average_grade DESC
LIMIT 1;