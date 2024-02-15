--Знайти список курсів, які відвідує студент.

SELECT subjects.name, students.name AS student_name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
WHERE students.id = 3;