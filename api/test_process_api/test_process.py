from fastapi import APIRouter
#create a router (component)
test_router = APIRouter(prefix="/test",
                        tags=["Tests"])
# getting of tests
test_router.get("/get-questions")
async def get_questions(level: str):
    pass
# check of questions
@test_router.post("/check-answer")
async def check_answer(user_id: int, question_id: int,
                       user_answer: str, correctness: bool):
    pass
#add question
@test_router.post("/add-question")
async def add_question(q_text: str, answer: int, v1: str, v2: str, v3: str = None, v4: str = None):
    pass