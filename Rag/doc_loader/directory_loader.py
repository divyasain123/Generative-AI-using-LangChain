from langchain_community.document_loaders import DirectoryLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

loader=DirectoryLoader("path",glob='*.pdf',
                       loader_cls="PyPDFLoader")
docs=loader.load()
print(docs[0].page_content)


#lazy load ek load krega aur sidha print krega phir next load krega jab zarurat hogi


#lazy load= ek loading technique where data is loaded only when it is needed, rather than all at once at the beginning. This can help improve performance and reduce memory usage, especially when dealing with large datasets or files.
#eager load= ek loading technique where all data is loaded at once at the beginning, rather than waiting until it is needed. This can be useful when working with small datasets or files, as it can help improve performance by reducing the number of times data needs to be accessed.#In summary, lazy loading defers data loading until necessary, while eager loading loads all data upfront
#The DirectoryLoader class from langchain_community.document_loaders is used to load documents from a specified directory. It supports various file formats and allows for customization of the loading process through parameters such as glob patterns and loader classes.#The loader_cls parameter specifies the class used to load individual files. In this case, "PyPDFLoader" is used to load PDF files.#The glob parameter allows for filtering files based on patterns. Here, '*.pdf' is used to
#load only PDF files from the specified directory.  
