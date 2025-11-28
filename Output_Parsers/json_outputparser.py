from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()
import os

model=ChatOpenAI(
    model="gryphe/mythomax-l2-13b",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1"
)


json_parser=JsonOutputParser()

#-----------------------------------------------------------------------------format_instructions is additonal instructions

template1=PromptTemplate(template="Give me the name and age of a fictional character./n{format_instructions}",
            input_variables=[],  partial_variables={'format_instructions':json_parser.get_format_instructions()})
#--------------------------------------------------------------partial_variables is used to pass format_instructions to the template and it is not faling at runtime ye phle is fail ho jata h 

"""prompt=template1.format()
result=model.invoke(prompt)
parsed=json_parser.parse(result.content)"""

#can use chain also
chain=template1 | model | json_parser
parsed=chain.invoke({})
print(parsed)
print(type(parsed))



