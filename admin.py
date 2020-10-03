from db import db
from flask import session, request

def delete_course(id):
    try:
        sql = "DELETE FROM courses WHERE id = :id"
        db.session.execute(sql,{"id":id})
        db.session.commit()
        return True
    except:
        return False

def delete_user(id):
    try:
        sql = "DELETE FROM users WHERE id = :id"
        db.session.execute(sql,{"id":id})
        db.session.commit()
        return True
    except:
        return False