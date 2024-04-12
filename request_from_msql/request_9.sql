SELECT 'course - ' || 'history' AS history_grades,
        'course - ' || 'math' AS math_grades,
        'course - ' || 'literature' AS literature_grades,
        'course - ' || 'physics' AS physics_grades,
        'course - ' || 'chemistry' AS chemistry_grades,
       'first_name - ' || s.first_name AS first_name,
       'last_name - ' || s.last_name AS last_name
FROM evaluations e
JOIN students s ON e.student_id = s.id
WHERE e.student_id = {subject};