import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.mysql import database
from app.controllers import controller

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

database.Base.metadata.create_all(bind=database.engine)   # to create tables automatically if not exist in db

app.include_router(controller.router)

    
    