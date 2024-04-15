from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from utils.query import answer_question
from models.model import QuestionRequest
from mysql import database
from mysql.savefiles import get_history_by_filename

router = APIRouter()
db = database.SessionLocal()


@router.post("/chat")
async def ask_question(request: QuestionRequest):
    try:
        if not request.question or not request.filename:
            raise HTTPException(status_code=400, detail="filename and question parameters are required")
       
        answer = answer_question(request.category,request.filename, request.question)
        
        return JSONResponse(status_code=200, content={"answer": answer})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")