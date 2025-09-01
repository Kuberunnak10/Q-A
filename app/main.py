from fastapi import FastAPI
from app.questions import router as questions_router
from app.answers import router as answers_router

app = FastAPI()

app.include_router(questions_router)
app.include_router(answers_router)

