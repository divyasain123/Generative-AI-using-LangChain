from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema



load_dotenv()
import os

model=ChatOpenAI(
    model="gryphe/mythomax-l2-13b", 
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1"
)
struc_parser=StructuredOutputParser.from_names_and_types(
    names_and_types={
        "name": "str",
        "age": "int"
    }       
)