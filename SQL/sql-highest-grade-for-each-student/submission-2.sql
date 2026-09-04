-- Window Function Solution
SELECT student_id, exam_id, score
FROM (
    SELECT
        student_id,
        exam_id,
        score,
        ROW_NUMBER() OVER (
            PARTITION BY student_id
            ORDER BY score DESC, exam_id
        ) AS rn
    FROM exam_results
)
WHERE rn = 1  -- Only take the first sequential from each group
ORDER BY student_id;