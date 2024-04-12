SELECT 
    items.item AS subject,
    items.teacher_id,
    items.first_name,
    items.last_name,
    AVG(
        CASE 
            WHEN items.teacher_id = 1 THEN evaluations.history_grades
            WHEN items.teacher_id = 2 THEN evaluations.math_grades
            WHEN items.teacher_id = 3 THEN evaluations.literature_grades
            WHEN items.teacher_id = 4 THEN evaluations.physics_grades
            WHEN items.teacher_id = 5 THEN evaluations.chemistry_grades
        END
    ) AS average_grade
FROM 
    items
JOIN 
    evaluations ON 1  -- Умова для з'єднання, оскільки відсутній спільний ключ
WHERE 
    items.teacher_id IN (?)
GROUP BY 
    items.item, items.teacher_id;
