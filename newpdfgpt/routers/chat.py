from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from utils.query import answer_question
from models.model import QuestionRequest

router = APIRouter()



@router.post("/chat")
async def ask_question(request: QuestionRequest):
    try:
        if not request.question :
            raise HTTPException(status_code=400, detail="question parameter is required")
        
        answer = answer_question(request.category, request.question)
        
        return JSONResponse(status_code=200, content={"answer": answer})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")