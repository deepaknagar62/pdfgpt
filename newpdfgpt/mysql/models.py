from sqlalchemy import Boolean, Column,Integer, String
from sqlalchemy.orm import relationship
from mysql.database import Base 




class Files(Base):
    __tablename__ = "Files"
    id = Column(Integer,primary_key=True,index=True)
    filename = Column(String(255),index=True)
    createdAt = Column(String(255), unique=True, index=True)
   
   


class Categories(Base):
    __tablename__ = "Categories"
    id = Column(Integer,primary_key=True,index=True)
    filename = Column(String(255),index=True)
    createdAt = Column(String(255), unique=True, index=True)
      
      
class ChatHistory(Base):
    __tablename__ = "ChatHistory"
    id = Column(Integer,primary_key=True,index=True)
    filename = Column(String(255),index=True)
    question = Column(String(2000), index=True)  
    answer = Column(String(5000), index=True)  
   
    
    

   