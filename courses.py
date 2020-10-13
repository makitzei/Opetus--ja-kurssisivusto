from db import db
from flask import session

def new_course(title, description, level, content, keyword, teacher_id):
    try:
        sql = "INSERT INTO courses (title, description, level, content, keyword, teacher_id) "\
            "VALUES (:title, :description, :level, :content, :keyword, :teacher_id)"
        db.session.execute(sql, {"title":title, "description":description, "level":level,\
            "content":content,"keyword":keyword,"teacher_id":teacher_id})
        db.session.commit()
        return True
    except:
        return False

def get_courses():
    sql = "SELECT * FROM courses"
    result = db.session.execute(sql)
    courses = result.fetchall()
    return courses

def get_course_with_teacher(id):
    sql = "SELECT id, title FROM courses WHERE teacher_id =:teacher_id"
    result = db.session.execute(sql, {"teacher_id":id})
    courses = result.fetchall()
    return courses

def get_course_with_id(id):
    sql = "SELECT * FROM courses WHERE id =:id"
    result = db.session.execute(sql, {"id":id})
    course = result.fetchone()
    return course

def with_no_student(student_id):
    sql = "SELECT courses.id, courses.title, courses.description, courses.level, courses.keyword "\
        "FROM courses "\
        "JOIN student_course ON courses.id = student_course.course_id "\
        "WHERE student_course.student_id NOT IN (:student_id)"
    result = db.session.execute(sql, {"student_id":student_id})
    courses = result.fetchall()
    return courses