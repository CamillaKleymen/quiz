from database import get_db
from database.models import Questions
from datetime import datetime

#add question
def add_question_db(q_text: str, answer: int, level: str ,v1: str,  v2: str,  v3: str = None,  v4: str = None) -> str:
    db = next(get_db())
    try:
        new_question = Questions(q_text=q_text, answer=answer, level=level, v1=v1, v2=v2, v3=v3, v4=v4)
        db.add(new_question)
        db.commit()
        return "Question was successfully add"
    except:
        return "Question wasn't add"
#delete a question
def delete_question_db(question_id):
    db = next(get_db())
    exact_question = db.query(Questions).filter_by(id=question_id).first()
    if exact_question:
        db.delete(exact_question)
        db.commit()
        return True
    return False
# getting 20 questions
def get20_questions_db(level: str) -> tuple:
    db = next(get_db())
    all_questions = db.query(Questions).filter_by(level=level).all()
    # delete duplicates
    sorted_questions = set([question for question in all_questions])
    return tuple(sorted_questions[0:20])


