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