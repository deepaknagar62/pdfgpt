from fastapi.middleware.cors import CORSMiddleware
from routers import upload, chat,category 
from fastapi import FastAPI
import os

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/api")
app.include_router(chat.router, prefix="/api")
app.include_router(category.router, prefix="/api")


db_directory = 'database'

@app.get("/namespaces")
def get_namespaces():
    namespaces = [name for name in os.listdir(db_directory) if os.path.isdir(os.path.join(db_directory, name))]
    return {"namespaces": namespaces}