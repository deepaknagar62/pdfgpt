from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import models

load_dotenv()
import os
DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL,echo=True,pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()
# Base.metadata.create_all(bind=engine)        # to create tables automatically if not exist in db