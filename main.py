from fastapi import FastAPI, Body
from api.test_process_api.test_process import test_router
from api.users_api.users import user_router
from database import Base, engine

Base.metadata.create_all(bind=engine)
#create an object

app = FastAPI(docs_url="/")
app.include_router(user_router)
app.include_router(test_router)

@app.get("/home")
async def hello():
    return {"status": 1, "message": "hello"}

@app.get("/example")
async def param_example(user_id: int, user_answer: str):
    return {"status": 1, "message": f" User {user_id} has answer {user_answer}"}

#body request
@app.put("/test-body")
async def test_body(header: str = Body(...), main_text: str = Body(default="Text example")):
    return {header, main_text}
# example post request
@app.post("/home")
async def first_post(name: str, phone_number: int):
    return {name: phone_number}
@app.delete("/home")
async def first_post(name: str, phone_number: int):
    return {name: phone_number}

#run project through terminal uvicorn main: app --reload


