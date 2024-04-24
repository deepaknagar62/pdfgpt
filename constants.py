import os
from dotenv import load_dotenv

load_dotenv()


OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
MODEL_NAME=os.getenv("MODEL_NAME")

DB_URL = os.getenv("DB_URL")
