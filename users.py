from db import db
from flask import session 
from werkzeug.security import check_password_hash, generate_password_hash

def register(firstname, lastname, username, password, status):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (firstname,lastname,username,password,status) VALUES (:firstname,:lastname,:username,:password,:status)"
        db.session.execute(sql, {"firstname":firstname,"lastname":lastname,"username":username,"password":hash_value,"status":status})
        db.session.commit()
    except:
        return False
    return login(username,password)

def login(username,password):
    sql = "SELECT password, id FROM users WHERE username =:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        hash_value = user[0]
    if check_password_hash(user[0],password):
        session["user_id"] = user[1]
        return True
    else:
        return False

def user_id():
    return session.get("user_id", 0)

def user_all(id):
    sql = "SELECT * FROM users WHERE id =:id"
    result = db.session.execute(sql, {"id":id})
    user = result.fetchone()
    return user

def user_firstname(user):
    return user[1]

def logout():
    del session["user_id"]

def is_admin(id):
    allow = False
    sql = "SELECT status FROM users WHERE id = :id"
    result = db.session.execute(sql, {"id":id})
    status = result.fetchone()
    if status[0] == "admin":
        allow = True
    return allow

def is_teacher(id):
    allow = False
    sql = "SELECT status FROM users WHERE id = :id"
    result = db.session.execute(sql, {"id":id})
    status = result.fetchone()
    if status[0] == "opettaja":
        allow = True
    return allow

def is_student(id):
    allow = False
    sql = "SELECT status FROM users WHERE id = :id"
    result = db.session.execute(sql, {"id":id})
    status = result.fetchone()
    if status[0] == "oppilas":
        allow = True
    return allow

def get_users():
    sql = "SELECT * FROM users"
    result = db.session.execute(sql)
    users = result.fetchall()
    return users
