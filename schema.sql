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
    teacher_id INTEGER REFERENCES users
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    question TEXT,
    course_id INTEGER REFERENCES courses 
);

CREATE TABLE choices (
    id SERIAL PRIMARY KEY,
    choice TEXT,
    correct BOOLEAN,
    question_id INTEGER REFERENCES questions
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    choice_id INTEGER REFERENCES choices
);

CREATE TABLE student_course (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES users,
    course_id INTEGER REFERENCES courses
);


