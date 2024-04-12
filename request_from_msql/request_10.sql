SELECT DISTINCT
    'Course',
    i.item AS course,
    'Teacher',
    i.first_name,
    i.last_name,
    'Grades',
        CASE 
            WHEN i.item = 'Исторія' THEN e.history_grades
            WHEN i.item = 'Математика' THEN e.math_grades
            WHEN i.item = 'Література' THEN e.literature_grades
            WHEN i.item = 'Фізика' THEN e.physics_grades
            WHEN i.item = 'Хімія' THEN e.chemistry_grades
        END
FROM
    items i
JOIN
    evaluations e ON i.item IN ('Исторія', 'Математика', 'Література', 'Фізика', 'Хімія')
WHERE
    e.student_id = ?  
    AND i.teacher_id IN (?) 

-- SELECT DISTINCT
--     i.item AS course
-- FROM
--     items i
-- JOIN
--     evaluations e ON i.item IN ('history', 'math', 'literature', 'physics', 'chemistry')
-- WHERE
--     e.student_id = ?  -- ИД студента
--     AND i.teacher_id = ?  -- ИД викладателя