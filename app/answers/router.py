from fastapi import APIRouter, HTTPException, Depends
from app.answers import schemas
from app.answers.dao import AnswerDAO
from app.questions.dao import QuestionDAO
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/questions/{question_id}/answers/", response_model=schemas.Answer)
async def create_answer(question_id: int, answer: schemas.AnswerCreate, db: AsyncSession = Depends(get_db)):
    # Check if question exists
    question = await QuestionDAO.find_by_id(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    created = await AnswerDAO.add(db, question_id=question_id, **answer.model_dump())
    return created

@router.get("/answers/{answer_id}", response_model=schemas.Answer)
async def get_answer(answer_id: int, db: AsyncSession = Depends(get_db)):
    answer = await AnswerDAO.find_by_id(db, answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    return answer

@router.delete("/answers/{answer_id}")
async def delete_answer(answer_id: int, db: AsyncSession = Depends(get_db)):
    await AnswerDAO.delete(db, id=answer_id)
    return {"msg": "Answer deleted"}
