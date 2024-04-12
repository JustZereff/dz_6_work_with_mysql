SELECT
    g.group_name,
    AVG(e.{subject}) AS average_grade
FROM
    evaluations e
JOIN
    groups g ON e.student_id = g.student_id
WHERE
    g.group_name = ?  -- Замените на нужное название группы
    AND e.{subject} IS NOT NULL  -- Убедитесь, что выбираются только непустые оценки по математике
GROUP BY
    g.group_name;


-- SELECT
--     g.group_name,
--     AVG((e.history_grades + e.math_grades + e.literature_grades + e.physics_grades + e.chemistry_grades) / 5) AS average_group_grade
-- FROM
--     evaluations e
-- JOIN
--     groups g ON e.student_id = g.student_id
-- WHERE
--     g.group_name = 'group_b'  -- Замените на нужное название группы
-- GROUP BY
--     g.group_name;