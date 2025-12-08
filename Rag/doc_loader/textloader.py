from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
loader=TextLoader(r"C:\Users\DIVYA\OneDrive\Desktop\Generative-AI-using-LangChain\Rag\doc_loader\ppp.text")
doc=loader.load()
print(doc)
print(doc[0])
print(doc[0].page_content)
print(doc[0].metadata)
print(type(doc))
print(len(doc))

parser=StrOutputParser()

model=ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0)
template=PromptTemplate(template="Summarize the following text{docs}",input_variables=["docs"])

chain=template|model|parser
result=chain.invoke({"docs":doc})
print(result)