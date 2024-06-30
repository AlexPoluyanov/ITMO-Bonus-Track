/* 1. Выбрать всех студентов из одной группы, упорядочив по ФИО: */

SELECT groups.group_name, students.last_name, students.first_name,  students.middle_name
FROM students JOIN groups ON groups.id = students.group_id
WHERE groups.group_name = 'P3301' ORDER BY students.last_name, students.first_name,  students.middle_name;


/* 2. Упорядочить сданные кем-либо экзамены по числу сдавших: */

SELECT
    e.id,
    e.name,
    COUNT(r.id) AS passed_count
FROM
    exams e
LEFT JOIN
    results r ON e.id = r.exam_id AND r.passed = TRUE
GROUP BY
    e.id
ORDER BY
    passed_count DESC;


/* 3. Найти человека с наивычшей суммой баллов который закрыл сессию без долгов. Вывести его зачетку.*/

WITH all_passed_exams AS (
    SELECT r.student_id, SUM(r.score) AS total_score
    FROM results r
    JOIN exams e ON r.exam_id = e.id
    WHERE e.type IN ('Зачёт', 'Дифференцированный зачёт', 'Экзамен') AND r.passed = true
    GROUP BY r.student_id
)
SELECT e.name AS exam_name, r.passed, r.score
FROM results r
JOIN all_passed_exams ape ON r.student_id = ape.student_id
JOIN exams e ON r.exam_id = e.id
JOIN students s ON r.student_id = s.id
WHERE s.id = (
    SELECT s.id
    FROM all_passed_exams ape
    JOIN students s ON ape.student_id = s.id
    ORDER BY ape.total_score DESC
    LIMIT 1
)
ORDER BY r.score DESC;




/* 4. Найти самую малочисленную группу*/ 

SELECT
    g.group_name,
    COUNT(s.id) AS student_count
FROM
    groups g
LEFT JOIN
    students s ON g.id = s.group_id
GROUP BY
    g.id
ORDER BY
    student_count ASC
LIMIT 1;


/* 5. Найти студента, сдавшего больше всех экзаменов: */
SELECT
    s.id,
    s.last_name,
    s.first_name,
    COUNT(r.id) AS exams_passed
FROM
    students s
JOIN
    results r ON s.id = r.student_id AND r.passed = TRUE
GROUP BY
    s.id
ORDER BY
    exams_passed DESC
LIMIT 1;


/* 6. Найти всех студентов, сдавших все обязательные экзамены с хотя бы одним несданным зачетом: */

SELECT
    s.id,
    s.first_name,
    s.last_name
FROM
    students s
WHERE
    NOT EXISTS (
        SELECT 1
        FROM group_exams ge
        WHERE ge.group_id = s.group_id
          AND ge.required = TRUE
          AND ge.exam_id NOT IN (
              SELECT r.exam_id
              FROM results r
              WHERE r.student_id = s.id AND r.passed = TRUE
          )
    )
    AND EXISTS (
        SELECT 1
        FROM group_exams ge
        WHERE ge.group_id = s.group_id
          AND ge.required = TRUE
          AND ge.exam_id IN (
              SELECT r.exam_id
              FROM results r
              WHERE r.student_id = s.id AND r.passed = FALSE
              AND r.exam_id IN (SELECT id FROM exams WHERE type = 'Зачёт')
          )
    );


/* 7. Найти группу/группы с самой большой нагрузкой (числом зачетов и экзаменов): */

WITH exam_counts AS (
    SELECT
        g.id AS group_id,
        g.group_name,
        COUNT(ge.exam_id) AS exam_count
    FROM
        groups g
    JOIN
        group_exams ge ON g.id = ge.group_id
    GROUP BY
        g.id, g.group_name
)
SELECT
    group_id,
    group_name,
    exam_count
FROM
    exam_counts
WHERE
    exam_count = (SELECT MAX(exam_count) FROM exam_counts)
    ORDER BY group_id;


/* 8. Найти, сколько студентов и из каких стран учатся в вузе: */

SELECT citizenship, count(citizenship)
FROM students
GROUP BY citizenship
ORDER BY count(citizenship) DESC;


/* 9. Найти самый «сложный» экзамен (с максимальным процентом не сдавших). Полностью необязательные экзамены не рассматривать: */

SELECT
    e.id,
    e.name,
    (COUNT(r.id) FILTER (WHERE r.passed = FALSE) * 1.0 / COUNT(r.id)) AS fail_rate
FROM
    exams e
JOIN
    results r ON e.id = r.exam_id
WHERE
    e.id IN (
        SELECT DISTINCT exam_id FROM group_exams WHERE required = TRUE
    )
GROUP BY
    e.id
ORDER BY
    fail_rate DESC
LIMIT 1;



/* 10. Вывести список всех экзаменов студнта: */

SELECT e.name, e.type, e.place, e.date
FROM exams e
WHERE e.id IN (
    SELECT ge.exam_id
    FROM group_exams ge
    JOIN students s ON ge.group_id = s.group_id
    WHERE s.id = 2
    UNION ALL
    SELECT pe.exam_id
    FROM personal_exams pe
    WHERE pe.student_id = 2
) 
ORDER BY date, type;
