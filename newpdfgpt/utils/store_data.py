import os
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv


load_dotenv()


directory = './uploads'
db_directory = 'database'

def run(namespace):
    loader = DirectoryLoader(directory)
    documents = loader.load()
    
    text_splitter = CharacterTextSplitter(
    separator=".",
    chunk_size=4000,
    chunk_overlap=200,
    )
    docs = text_splitter.split_documents(documents)
    
    
   
    embeddings = OpenAIEmbeddings(
        model=os.getenv("PINECONE_MODEL_NAME"),
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    
   
    
     
    vectorstore = FAISS.from_documents(docs, embeddings)
  
    namespace_directory = os.path.join(db_directory, namespace)
    vectorstore.save_local(namespace_directory)
    
    
    print("Data stored in vector database......")
  
    




