from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
loader = UnstructuredPDFLoader(r"C:\Users\DIVYA\OneDrive\Desktop\datascience.2.pdf")
