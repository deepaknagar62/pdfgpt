from fastapi.middleware.cors import CORSMiddleware
from routers import upload, chat,category
from fastapi import FastAPI, Depends
import os
from sqlalchemy.orm import Session
from mysql import models, database


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

database.Base.metadata.create_all(bind=database.engine)   # to create tables automatically if not exist in db

app.include_router(upload.router, prefix="/api")
app.include_router(chat.router, prefix="/api")
app.include_router(category.router, prefix="/api")

    
    