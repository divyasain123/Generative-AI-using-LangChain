from langchain_text_splitters import RecursiveCharacterTextSplitter,Language
from dotenv import load_dotenv
load_dotenv()

code=r"""from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
load_dotenv()

loader=PyPDFLoader(r"C:\Users\DIVYA\OneDrive\Desktop\Generative-AI-using-LangChain\ENGLISH LESSON PLAN UPDATED.pdf")

text=loader.load()


split = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
    
)

result=split.split_documents(text)
print(len(result))
print(result)
"""

split = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=200,
    chunk_overlap=0
)

chunk=split.split_text(code)
print(len(chunk))
print(chunk[2])
