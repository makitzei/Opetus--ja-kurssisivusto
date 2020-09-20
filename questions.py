from db import db
from flask import session

def new_question(question, course_id, choices):
    try:
        sql = "INSERT INTO questions (question, course_id) VALUES (:question, :course_id) RETURNING id"
        result = db.session.execute(sql, {"question":question,"course_id":course_id})
        question_id = result.fetchone()[0]
        #for choice in choices:
        # miten käydään booleanit tässä kans läpi???
        #if choice != "":
        #    sql = "INSERT INTO choices (choice, correct, question_id) VALUES (:poll_id, :choice)"
        #    db.session.execute(sql, {"poll_id":poll_id, "choice":choice})
        db.session.commit()
        return True
    except:
        return False
