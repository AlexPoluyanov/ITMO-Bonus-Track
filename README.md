# ITMO-Bonustrack

Итоговый проект по Bonustrack (Методы анализа данных)

Тип проекта: Разработка базы данных

## Выполнили:

<table style="width: 100%; text-align: center;">
  <thead>
    <tr>
      <th style="width: 33.33%;"><img src="https://github.com/AlexPoluyanov/ITMO-BonusTrack/assets/109956453/dfdad839-25d7-4ac4-9d92-911f04ad4862" alt="image" style="max-width: 100%;"></th>
      <th style="width: 33.33%;"><img src="https://github.com/AlexPoluyanov/ITMO-BonusTrack/assets/109956453/bf52d02f-11b4-422f-a5c5-766dc88b1e95" alt="image" style="max-width: 100%;"></th>
      <th style="width: 33.33%;"><img src="https://github.com/AlexPoluyanov/ITMO-BonusTrack/assets/109956453/4ca909f2-9825-431f-87be-2165e39d6706" alt="image" style="max-width: 100%;"></th>
    </tr>
  </thead>
  <tbody>
      <tr>
      <td>Полуянов Александр Михайлович</td>
      <td>Пухова Виктория Олеговна</td>
      <td>Колосов Глеб Александрович</td>
    </tr>
    <tr>
      <td>341473</td>
      <td>335332</td>
      <td>336654</td>
    </tr>
    <tr>
      <td>P33141</td>
      <td>U33762</td>
      <td>U33762</td>
    </tr>
    <tr>
      <td><a href="https://t.me/AlexPoluyanov">t.me/AlexPoluyanov</a></td>
      <td><a href="https://t.me/phv_vic">t.me/phv_vic</a></td>
      <td><a href="https://t.me/eto_gleb">t.me/eto_gleb</a></td>
    </tr>
  </tbody>
</table>


# Содержание
<ul>
    <li><a href="">Выбор предметной области</a></li>
    <li><a href="">Описание типовых запросов</a></li>
    <li><a href="">Построение ER-диаграммы</a></li>
    <li><a href="">Выбор СУБД</a></li>
    <li><a href="">Создание структуры данных</a></li>
    <li><a href="">Создание таблиц</a></li>
    <li><a href="">Заполнение таблиц</a></li>
    <li><a href="">Реализация запросов</a></li>
    <li><a href="">Выводы и результаты работы</a></li>
</ul>



# Выбор предметной области

Предметная область была взята из списка предложенных. Описание предметной области:

Ваш долг – помочь родной кафедре в автоматизации отчетности по ходу и результатам сессии.
В базе данных должна храниться информация о получении студентами кафедры зачетов и сдаче экзаменов. Необходима также наличие допуска к экзаменам.  
Информация, которая может быть востребована:  
*	все об успеваемости любого студента – что ему нужно сдавать, что сдано, что осталось  
*	списки студентов с долгами по конкретным предметам  
*	списки студентов, сдавших сессию, с одним долгом, двумя и т.д.

Дополнение: каждый студент учится в одной из групп. Для каждой группы определены набор экзаменов и зачетов, обязательных для сдачи. Студент может также сдавать и получать зачеты по необязательным предметам.

# Описание типовых запросов
<ol>
  <li>Выбрать всех студентов из одной группы упорядочив по ФИО</li>
  <li>Упорядочить сданные кем-либо экзамены по числу сдавших.</li>
  <li>Найти человека с наивычшей суммой баллов который закрыл сессию без долгов. Вывести его зачетку.</li>
  <li>Найти самую малочисленную группу</li>
  <li>Найти студента, сдавшего больше всех экзаменов</li>
  <li>Найти курс который учащиеся пытаются сдать наибольшее количество раз </li>
  <li>Найти группу/группы с самой большой нагрузкой (числом зачетов и экзаменов).</li>
  <li>Найти, сколько студентов и из каких стран учатся в вузе.</li>
  <li>Найти самый «сложный» экзамен (с максимальным процентом не сдавших). Полностью необязательные экзамены не рассматривать.</li>
  <li>Вывести список всех экзаменов и зачетов студнта.</li>
  
</ol>

# Построение ER-диаграммы

![Untitled (5)](https://github.com/AlexPoluyanov/ITMO-BonusTrack/assets/109956453/5c515e12-da1d-4b7f-9f1c-8c361f16806e)  

# Выбор СУБД

Выбор PostgreSQL обоснован следующими причинами:

<ol>
    <li>Открытый исходный код и бесплатное использование: PostgreSQL - это бесплатная СУБД с открытым исходным кодом, что позволяет избежать затрат на лицензии и дает возможность гибкой настройки под конкретные нужды.</li>
<li>Поддержка сложных запросов: PostgreSQL отлично справляется с выполнением сложных запросов, что необходимо для анализа успеваемости студентов, формирования списков задолженностей и других отчетов.</li>
<li>Надежность и масштабируемость: PostgreSQL известна своей надежностью и возможностью масштабирования, что важно для хранения и обработки больших объемов данных о студентах и их успеваемости.</li>
<li>Мощные механизмы контроля доступа: СУБД предлагает развитую систему контроля доступа, что важно для обеспечения безопасности данных студентов.</li>
<li>Соответствие стандартам SQL: PostgreSQL соответствует стандартам SQL, что облегчает разработку и поддержку системы, а также интеграцию с другими инструментами и системами.</li>
<li>Активное сообщество и поддержка: Большое сообщество пользователей и разработчиков обеспечивает наличие документации, форумов и других ресурсов для решения возникающих вопросов.</li>
<li>Поддержка транзакций и согласованности данных: PostgreSQL обеспечивает полную поддержку транзакций и согласованности данных, что критически важно для обеспечения точности и надежности данных в системе.</li>
<li>Гибкие индексы и оптимизация запросов: Различные типы индексов и возможности оптимизации запросов позволяют повысить производительность системы при работе с большими объемами данных.</li>
</ol>


# Создание структуры данных

## Создание таблиц
C помощью файла запускается <a href="https://github.com/AlexPoluyanov/ITMO-BonusTrack/blob/main/scripts/create%20script.sql">скрипт</a>, который создает таблицы (отношения) с прописанными связями и базовыми ограничениями целостности данных.  
```sql
CREATE TYPE exam_type AS ENUM ('Зачёт', 'Экзамен', 'Дифференцированный зачёт'); 
-- Типы итогового контроля

CREATE TABLE "groups" (
  "id" SERIAL PRIMARY KEY,
  "group_name" VARCHAR(255) UNIQUE NOT NULL -- хранит литеру и номер группы. первая цифра отвечает за курс
);

CREATE TABLE "exams" (
  "id" SERIAL PRIMARY KEY,
  "type" exam_type, -- использование своего типа данных
  "name" VARCHAR(255) NOT NULL,
  "place" VARCHAR(255) NOT NULL,
  "date" DATE
);

CREATE TABLE "students" (
  "id" SERIAL PRIMARY KEY,
  "first_name" VARCHAR(255) NOT NULL,
  "last_name" VARCHAR(255) NOT NULL,
  "middle_name" VARCHAR(255),
  "date_of_birth" DATE NOT NULL,
  "citizenship" VARCHAR(255),
  "contract" BOOLEAN,
  "group_id" INT REFERENCES groups("id")
);

CREATE TABLE "results" (
  "id" SERIAL PRIMARY KEY,
  "student_id" INT REFERENCES students("id"),
  "exam_id" INT REFERENCES exams("id"),
  "passed" BOOLEAN NOT NULL,
  "score" INT -- оценка в 100 бальной системе
);

CREATE TABLE "personal_exams" (
  "student_id" INT REFERENCES students("id"),
  "exam_id" INT REFERENCES exams("id"),
  "required" BOOLEAN NOT NULL,
  PRIMARY KEY ("student_id", "exam_id") -- уникальный ключ из сочитания уникального номера студента и экзамена
);

CREATE TABLE "group_exams" (
  "group_id" INT REFERENCES groups("id"),
  "exam_id" INT REFERENCES exams("id"),
  "required" BOOLEAN NOT NULL,
  PRIMARY KEY ("group_id", "exam_id")
);

CREATE TABLE "exam_access" (
  "id" SERIAL PRIMARY KEY,
  "stud_id" INT REFERENCES students("id"),
  "exam_id" INT REFERENCES exams("id"),
  "has_access" BOOLEAN 
);

CREATE TABLE "access_requirements" (
  "id" SERIAL PRIMARY KEY,
  "exam_id" INT REFERENCES exams("id"),
  "required_exam_id" INT REFERENCES exams("id") -- идентификатор экзамена без сдачи которого нельзя сдать другой экзамен
);
```

## Заполнение таблиц

Для заполнения таблиц рандомизированными псевдо реальными значениями был разработан Python скрипт, генерирующий последовательности SQL-запросов.  

`Ссылка на файл` <a href = "https://github.com/AlexPoluyanov/ITMO-BonusTrack/blob/main/data%20generator.py">Python</a>  

`Поный скрипт заполнения` можно найти по <a href = "https://github.com/AlexPoluyanov/ITMO-BonusTrack/blob/main/scripts/inserts%20script.sql">ссылке</a>


Заполнение таблицы groups
```sql
INSERT INTO groups(group_name) VALUES
('N1101'),
('N1102'),
('N1103'),
('N1104'),
('N1105'),
('N1106'),
('N1107'),
('N1108'),
('N1201'),
('N1202')...
```

Заполнение таблицы exams
```sql
INSERT INTO exams(name,type,place,date) VALUES
('Математика', 'Зачёт', 'Online ZoomRoom #245', '2024-06-03 10:30'),
('Хранение и обработка данных', 'Экзамен', 'Кронверкский пр., 49, Аудитория 137', '2024-06-27 16:30'),
('Английский язык', 'Зачёт', 'Кронверкский пр., 49, Аудитория 187', '2024-06-06 13:00'),
('Физкультура', 'Дифференцированный зачёт', 'Ломоносова, 9, Аудитория 212', '2024-06-06 17:00'),
('Математика', 'Дифференцированный зачёт', 'Online ZoomRoom #338', '2024-06-24 10:30')...
```

Заполнение таблицы students
```sql
INSERT INTO students(first_name, last_name, middle_name, date_of_birth, citizenship, contract, group_id) VALUES
('Яна', 'Александрова', 'Мироновна', '2001-01-12', 'Таджикистан',  True, 92),
('Анастасия', 'Третьякова', 'Марковна', '2000-12-25', 'Азербайджан',  False, 83),
('Лариса', 'Вишнякова', 'Иосифовна', '2001-04-07', 'Россия',  True, 102),
('Дарья', 'Кулакова', 'Михайловна', '2002-02-17', 'Туркменистан',  False, 51),
('Валерия', 'Филатова', 'Артуровна', '2002-10-07', 'Эстония',  True, 25),
('Людмила', 'Мартынова', 'Максимовна', '2000-02-15', 'Россия',  False, 87)...
```

Заполнение таблицы results и exam_access
```sql
DO $$
DECLARE
    student RECORD;
    exam INTEGER;
    has_access BOOLEAN;
    score NUMERIC;
BEGIN
    FOR student IN SELECT * FROM students LOOP
        FOR exam IN (
            SELECT exam_id FROM group_exams
            WHERE group_id = student.group_id
            UNION ALL
            SELECT exam_id FROM personal_exams
            WHERE student_id = student.id
        ) LOOP
            has_access := (RANDOM() > 0.15);
            INSERT INTO exam_access(student_id, exam_id, has_access)
            VALUES (student.id, exam, has_access);
            IF has_access = TRUE THEN
                score := ((RANDOM()*100+30)::NUMERIC % 100);
                IF score >= 60 THEN
                    INSERT INTO results(student_id, exam_id, passed, score)
                    VALUES (student.id, exam, TRUE, score);
                ELSE
                    INSERT INTO results(student_id, exam_id, passed, score)
                    VALUES (student.id, exam, FALSE, score);
                END IF;
            ELSE
                INSERT INTO results(student_id, exam_id, passed, score)
                VALUES (student.id, exam, FALSE, NULL);
            END IF;
        END LOOP;
    END LOOP;
END $$;
```  

Заполнение таблицы group_exams
```sql
INSERT INTO group_exams(group_id, exam_id, required) VALUES
(1, 1, True),
(1, 2, False),
(1, 3, False),
(1, 4, True),
(2, 5, False),
(2, 6, True)...
```

Заполнение таблицы personal exams
```sql
INSERT INTO exams(name, type, place, date) VALUES
('Экономика', 'Экзамен', 'Кронверкский пр., 49, Аудитория 137', '2024-06-27 10:30'),
('Немецкий язык', 'Зачёт', 'Кронверкский пр., 49, Аудитория 187', '2024-06-06 10:00'),
('Профильная математика', 'Экзамен', 'Ломоносова, 9, Аудитория 212', '2024-06-06 10:00');
```
```sql
DO $$
DECLARE
    student RECORD;
BEGIN
    FOR student IN SELECT * FROM STUDENTS LOOP
        IF student.id % 11 = 0 THEN
            INSERT INTO personal_exams(student_id, exam_id, required)
            VALUES (student.id, 360, TRUE);
        END IF;
        IF student.id % 16 = 0 THEN
            INSERT INTO personal_exams(student_id, exam_id, required)
            VALUES (student.id, 361, TRUE);
        END IF;
        IF student.id % 21 = 0 THEN
            INSERT INTO personal_exams(student_id, exam_id, required)
            VALUES (student.id, 362, TRUE);
        END IF;
    END LOOP;
END $$;

```


Заполнение таблицы access_requirements
```sql
INSERT INTO access_requirements(exam_id, required_exam_id) VALUES
(362, 355),
(362, 352);
```

## Реализация запросов

```sql
/* 1. Выбрать всех студентов из одной группы, упорядочив по ФИО: */

SELECT groups.group_name, students.last_name, students.first_name,  students.middle_name
FROM students JOIN groups ON groups.id = students.group_id
WHERE groups.group_name = 'P3301' ORDER BY students.last_name, students.first_name,  students.middle_name;
```

![image](https://github.com/AlexPoluyanov/ITMO-BonusTrack/assets/109956453/b6f5bfd0-539b-43e6-b50c-63ac9fa74606)



```sql
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
```

![image](https://github.com/AlexPoluyanov/ITMO-BonusTrack/assets/109956453/69a4d97e-6d64-4efb-bd6f-25303b983015)



```sql
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
```

![image](https://github.com/AlexPoluyanov/ITMO-BonusTrack/assets/109956453/af4d6cc7-ef8d-474a-9f57-27698fe1ec01)



```sql
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
```

![image](https://github.com/AlexPoluyanov/ITMO-BonusTrack/assets/109956453/091971d8-874c-4eb8-924d-887d9092b649)



```sql
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
```

![image](https://github.com/AlexPoluyanov/ITMO-BonusTrack/assets/109956453/657a30df-22ca-4877-90b3-22caac58227c)



```sql
/* 6. Найти курс который учащиеся пытаются сдать наибольшее количество раз */

SELECT e.name AS exam_name, COUNT(r.student_id) AS num_students_attempted
FROM exams e
LEFT JOIN results r ON e.id = r.exam_id
GROUP BY e.id, e.name
ORDER BY num_students_attempted DESC
LIMIT 1;
```

![image](https://github.com/AlexPoluyanov/ITMO-BonusTrack/assets/109956453/32bf3067-41db-4e01-9b3e-b22716b8cd2e)



```sql
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
```

![image](https://github.com/AlexPoluyanov/ITMO-BonusTrack/assets/109956453/b54dfa2a-bb72-4f15-bc77-13ca24b77302)



```sql
/* 8. Найти, сколько студентов и из каких стран учатся в вузе: */

SELECT citizenship, count(citizenship)
FROM students
GROUP BY citizenship
ORDER BY count(citizenship) DESC;
```

![image](https://github.com/AlexPoluyanov/ITMO-BonusTrack/assets/109956453/437bb40a-70c8-4b04-ba7d-b0804d4b82bd)



```sql
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
```

![image](https://github.com/AlexPoluyanov/ITMO-BonusTrack/assets/109956453/f3c02df4-69cd-451c-91b5-a433a2b81551)



```sql
/* 10. Вывести список всех экзаменов и зачетов студента: */

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
```

![image](https://github.com/AlexPoluyanov/ITMO-BonusTrack/assets/109956453/0bbd430d-3d7e-4a5a-8960-744fb1bde67c)

# Выводы и результаты работы

Для автоматизации отчетности по успеваемости студентов кафедры была создана база данных, охватывающая информацию о сдаче зачетов и экзаменов. В проекте использована PostgreSQL, выбранная из-за её открытого исходного кода, мощных возможностей выполнения сложных запросов, надежности и масштабируемости. Структура данных включает таблицы для групп, студентов, экзаменов, результатов и других сущностей, связанных с требованиями доступа и персональными экзаменами.  

Реализовано несколько типовых запросов, таких как выборка студентов по группам, упорядоченных по ФИО, и анализ успеваемости (например, поиск студентов с наивысшими баллами, закрывших сессию без долгов). Также выполнены запросы на определение самых малочисленных групп, нахождение самого "сложного" экзамена и анализ стран происхождения студентов.  

Реализация проекта позволяет эффективно управлять данными о студентах, их успехах и задолженностях, что важно для улучшения управления учебным процессом и предоставления актуальной отчетности кафедре. 

За время работы над проектом мы укрепили свои знания в рамках разработки БД и использования языка Python для авоматизации процессов. Данные навыки помогут нам в будущей профессии.  
