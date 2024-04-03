import os
from pinecone import Pinecone, ServerlessSpec
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_pinecone import PineconeVectorStore
from langchain_community.vectorstores import FAISS
import faiss
from dotenv import load_dotenv





load_dotenv()
db_directory = 'database'

def answer_question(category, namespace , question):
    try:
        
        embeddings = OpenAIEmbeddings(
            model=os.getenv("PINECONE_MODEL_NAME"),
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        
        if category is None:
            namespace_directory = os.path.join(db_directory, namespace)
        else:
            namespace_directory = os.path.join(db_directory,category, namespace)
            
        
        vectorstore = FAISS.load_local(namespace_directory, embeddings,allow_dangerous_deserialization=True)
        
        # file_path = os.path.join(namespace_directory, 'index.faiss')
        # index = faiss.read_index(file_path)
        # print(index)
        
        query_result = vectorstore.similarity_search(query=question, k=3)
        llm = ChatOpenAI(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            model_name='gpt-3.5-turbo',
            temperature=0.1
        )
        
        chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(),
             
            # return_source_documents=True
        )

        answer = chain.invoke(question)
        
        return answer
    except Exception as e:
        raise e
