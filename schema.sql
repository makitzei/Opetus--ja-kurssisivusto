CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    firstname TEXT, 
    lastname TEXT, 
    username TEXT UNIQUE, 
    password TEXT, 
    status TEXT
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    title TEXT,
    description TEXT,
    level INTEGER,
    content TEXT,
    keyword TEXT,
    teacher_id INTEGER REFERENCES users ON DELETE CASCADE 
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    question TEXT,
    course_id INTEGER REFERENCES courses ON DELETE CASCADE 
);

CREATE TABLE choices (
    id SERIAL PRIMARY KEY,
    choice TEXT,
    correct BOOLEAN,
    question_id INTEGER REFERENCES questions ON DELETE CASCADE 
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses ON DELETE CASCADE, 
    student_id INTEGER REFERENCES users ON DELETE CASCADE,
    question_id INTEGER REFERENCES questions ON DELETE CASCADE,
    choice_id INTEGER REFERENCES choices ON DELETE CASCADE,
    sent_at TIMESTAMP 
);

CREATE TABLE student_course (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES users ON DELETE CASCADE ,
    course_id INTEGER REFERENCES courses ON DELETE CASCADE,
    CONSTRAINT ux_student_course UNIQUE (student_id,course_id) 
);

INSERT INTO users (firstname,lastname,username,password,status) VALUES ('Testi','Käyttäjä','admin','pass','admin');

