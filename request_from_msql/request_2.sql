SELECT e.student_id, 
       s.first_name, 
       s.last_name,
       ((e.{subject}_grades) / 1) AS average_grade
FROM evaluations e
JOIN students s ON e.student_id = s.id
WHERE e.{subject}_grades = (
    SELECT MAX(e2.{subject}_grades) 
    FROM evaluations e2
)
