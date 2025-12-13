from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
load_dotenv()

loader=PyPDFLoader(r"C:\Users\DIVYA\OneDrive\Desktop\Generative-AI-using-LangChain\ENGLISH LESSON PLAN UPDATED.pdf")

text=loader.load()


split = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result=split.split_documents(text)
print(result[5].page_content)

