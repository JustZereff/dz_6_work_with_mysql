SELECT 'id - ' || e.student_id AS student_id,
       'first_name - ' || s.first_name AS first_name,
       'last_name - ' || s.last_name AS last_name,
       'GPA - ' || ((e.history_grades + e.math_grades + e.literature_grades + e.physics_grades + e.chemistry_grades) / 5) AS average_grade
FROM evaluations e
JOIN students s ON e.student_id = s.id
ORDER BY average_grade DESC
LIMIT 1;