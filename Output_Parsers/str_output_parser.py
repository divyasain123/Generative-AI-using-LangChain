from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()
import os
from langchain_core.output_parsers import StrOutputParser
"""llm=HuggingFaceEndpoint(repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                        task="text-generation")
model=ChatHuggingFace(llm=llm)
"""
model=ChatOpenAI(
    model="gryphe/mythomax-l2-13b",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1"
)
#1st prompt-> detailed report
template1=PromptTemplate(
    template="write a detialed report about {topic}",   input_variables=["topic"]
)

#2nd prompt-> summary of the report
template2=PromptTemplate(
    template="summarize the following report in 5 lines:\n\n{report}",   input_variables=["report"]
)
parser=StrOutputParser()

chain=template1|model|parser|template2|model|parser
result=chain.invoke({"topic":"artificial intelligence"})
print(result)



