from fastapi import APIRouter, HTTPException, Depends
from app.questions import schemas
from app.questions.dao import QuestionDAO
from app.database import get_db

router = APIRouter()

@router.post("/questions/", response_model=schemas.Question)
async def create_question(question: schemas.QuestionCreate, db=Depends(get_db)):
    question_id = await QuestionDAO.add(db, **question.dict())
    return {**question.dict(), "id": question_id}

@router.get("/questions/", response_model=list[schemas.Question])
async def get_questions(db=Depends(get_db)):
    questions = await QuestionDAO.find_all(db)
    return questions

@router.get("/questions/{question_id}", response_model=schemas.Question)
async def get_question(question_id: int, db=Depends(get_db)):
    question = await QuestionDAO.find_with_answers(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@router.delete("/questions/{question_id}")
async def delete_question(question_id: int, db=Depends(get_db)):
    question = await QuestionDAO.find_by_id(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    await QuestionDAO.delete(db, id=question_id)
    return {"msg": "Question deleted"}
