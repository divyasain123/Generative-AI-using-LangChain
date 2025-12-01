#------A simple chain is sequential chain which connects multiple components in a sequence. The output of one component becomes the input of the next component.


from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, EmailStr, Field
load_dotenv()
from langchain_core.prompts import PromptTemplate
import os
model = ChatOpenAI(
    model="gryphe/mythomax-l2-13b",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1"
)

class person(BaseModel):
    name:str = Field(description="name of the person")
    age:int=Field(gt=18,description="age of the person")
    city:str=Field(description="city of the person")

parser = PydanticOutputParser(pydantic_object=person)   # we tellig here person class is our pydantic object

template=PromptTemplate(template="Generate a fictional person with name, age and city {place}.\n{format_instructions}",input_variables=["place"],partial_variables={"format_instructions":parser.get_format_instructions()})

chain=template|model|parser
result=chain.invoke({'place':'India'})
print(result)  # it will give output in the form of pydantic object
   
