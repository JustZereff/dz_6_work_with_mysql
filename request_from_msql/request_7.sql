SELECT
    'grades',
    evaluations.{subject} AS grades

FROM
    evaluations
JOIN
    groups ON evaluations.student_id = groups.student_id
WHERE
    groups.group_name = ?
