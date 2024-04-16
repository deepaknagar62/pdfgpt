import os
from pinecone import Pinecone, ServerlessSpec
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_pinecone import PineconeVectorStore
from langchain_community.vectorstores import FAISS
import faiss
from mysql.savefiles import save_history,get_history_by_filename
from mysql import database
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate 



prompt_template = """You are helpful information giving QA System and make sure you don't answer anything 
not related to following context. You are always provide useful information & details available in the given context. Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that Hmm, I am not sure, don't try to make up an answer.

{context}

Question: {question}
Helpful Answer:"""

qa_prompt = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)


load_dotenv()
db = database.SessionLocal()
db_directory = 'database'

 
def answer_question(category, namespace , question):
    try:
        
        embeddings = OpenAIEmbeddings(
            model=os.getenv("MODEL_NAME"),
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
         
        
         
        if category is None:
            namespace_directory = os.path.join(db_directory, namespace)
        
        else:
            namespace_directory = os.path.join(db_directory,category, namespace)
            
        
        vectorstore = FAISS.load_local(namespace_directory, embeddings,allow_dangerous_deserialization=True)
        
        # history = get_history_by_filename(namespace,db)
        # print(history)
        # query_result = vectorstore.similarity_search(query=question, k=3)
        
        llm = ChatOpenAI(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            model_name='gpt-3.5-turbo',
            temperature=0.1
        )
        
        chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(),
            chain_type_kwargs={"prompt": qa_prompt}, 
            # return_source_documents=True
        )

        result = chain.invoke(question)
        answer = result.get( "result",'')
        
        save_history(namespace, question, answer,db)
    
        return result
    except Exception as e:
        raise e
