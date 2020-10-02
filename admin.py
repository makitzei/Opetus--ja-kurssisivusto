from db import db
from flask import session, request

def delete_course(course_id):
    try:
        sql = "DELETE FROM courses WHERE course_id = :course_id"
        db.session.execute(sql,{"course_id":course_id})
        db.session.commit()
        return True
    except:
        return False