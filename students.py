from db import db
from flask import session, request

def join(student_id,course_id):
    try:
        sql = "INSERT INTO student_course(student_id, course_id) VALUES (:student_id, :course_id)"
        db.session.execute(sql,{"student_id":student_id,"course_id":course_id})
        db.session.commit()
        return True
    except:
        return False

def get_courses(student_id):
    sql = "SELECT courses.id, courses.title FROM courses JOIN student_course ON courses.id = student_course.course_id JOIN users ON student_course.student_id = users.id WHERE users.id = :student_id;"
    result = db.session.execute(sql,{"student_id":student_id})
    mycourses = result.fetchall()
    return mycourses

def leave_course(student_id, course_id):
    try:
        sql = "DELETE FROM student_course WHERE student_id = :student_id AND course_id = :course_id"
        db.session.execute(sql,{"student_id":student_id,"course_id":course_id})
        db.session.commit()
        return True
    except:
        return False

