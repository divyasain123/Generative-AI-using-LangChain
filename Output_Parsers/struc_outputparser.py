from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(
    model="gryphe/mythomax-l2-13b",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1"
)

schema = [
    ResponseSchema(name='name1', description='one fact about the fictional character'),
    ResponseSchema(name='name2', description='one fact about the fictional character'),
    ResponseSchema(name='name3', description='one fact about the fictional character'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template1 = PromptTemplate(
    template="write a fact about {topic}\n{formal_instructions}",
    input_variables=["topic"],
    partial_variables={"formal_instructions": parser.get_format_instructions()},
)

chain = template1 | model | parser
parsed = chain.invoke({"topic": "harry potter"})

print(parsed)
print(type(parsed))
