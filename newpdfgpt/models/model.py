from pydantic import BaseModel

class QuestionRequest(BaseModel):
    category: str
    question: str
