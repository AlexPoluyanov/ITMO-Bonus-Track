# ITMO-Bonustrack
Итоговый проект по Bonustrack (Методы анализа данных)

Тип проекта: Разработка базы данных

## Выполнили:

Полуянов Александр Михайлович 

341473 P33141 <a href="t.me/AlexPoluyanov">t.me/AlexPoluyanov</a>

Пухова Виктория Олеговна 

335332 U33762 <a href="t.me/phv_vic">t.me/phv_vic</a>

Колосов Глеб Александрович

336654 U33762 <a href="t.me/eto_gleb">t.me/eto_gleb</a>


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
  <li>Каково число студентов, не получивших ни одного зачета</li>
  <li>Найти самую малочисленную группу</li>
  <li>Найти студента, сдавшего больше всех экзаменов</li>
  <li>Найти всех студентов, сдавших все обязательные экзамены с хотя бы одним несданным зачетом</li>
  <li>Найти группу с самой большой нагрузкой (числом зачетов и экзаменов).</li>
  <li>Найти, сколько студентов и из каких стран учатся в вузе.</li>
  <li>Найти самый «сложный» экзамен (с максимальным процентом не сдавших). Полностью необязательные экзамены не рассматривать.</li>
  <li>Проверить, есть ли в базе студент, не допущенный ни к одному обязательному для его группы экзамену. Можно считать, что каждая группа обязана сдавать хотя бы один экзамен.</li>
  
</ol>

# Построение ER-диаграммы

![Untitled (5)](https://github.com/AlexPoluyanov/ITMO-BonusTrack/assets/109956453/5c515e12-da1d-4b7f-9f1c-8c361f16806e)  

# Выбор СУБД

# Создание структуры данных

## Создание таблиц
C помощью файла запускается скрипт, который создает таблицы (отношения) с прописанными связями и базовыми ограничениями целостности данных.  
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

## Заполнение таблиц groups

Для заполнения таблиц рандомизированными псевдо реальными значениями был разработан Python скрипт, генерирующий последовательности SQL-запросов.  

`Ссылка на файл` <a href = "">Python</a>  

`Поный скрипт заполнения` можно найти по <a href = "">ссылке</a>

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

