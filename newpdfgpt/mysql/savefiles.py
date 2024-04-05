
from fastapi import FastAPI,HTTPException, Depends
from datetime import datetime
from sqlalchemy.orm import Session
from mysql import models, database
from datetime import datetime


current_date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    

def insert_file_name(filename: str, db: Session):
    try:
        new_item = models.Files(filename=filename, createdAt=current_date_time)
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        
        print("file name saved in mysql database...............")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    
    
    


def insert_category(filename: str, db: Session):
    try:
        new_item = models.Categories(filename=filename, createdAt=current_date_time)
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        
        print("category saved in mysql database...............")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")    
    
    

def save_history(filename: str, question: str, answer:str, db:Session):
    try:
        chatHistory = models.ChatHistory(filename=filename, question=question, answer=answer)
        db.add(chatHistory)
        db.commit()
        db.refresh(chatHistory)
        
        print("chat history saved in databse...............")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")            