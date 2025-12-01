from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import os
from langchain_core.prompts import PromptTemplate

model = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1"
)




