from db import db
from flask import session, request

def get_result(answer_id):
    sql = "SELECT choices.choice, choices.correct FROM choices JOIN answers ON choices.id=answers.choice_id "\
        "WHERE answers.id=:answer_id"
    result = db.session.execute(sql, {"answer_id":answer_id})
    choice = result.fetchone()
    return choice