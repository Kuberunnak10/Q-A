from fastapi import FastAPI
from app.questions.router import router as questions_router
from app.answers.router import router as answers_router

app = FastAPI(
    title="QnA API",
    description="API service for questions and answers",
)

app.include_router(questions_router, prefix="/api/v1")
app.include_router(answers_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Q&A API is running"}

