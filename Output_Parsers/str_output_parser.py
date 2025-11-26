from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
llm=HuggingFaceEndpoint(repo_id="Tinylambda/Tinylambda-7B-Chat",
                        task="text-generation")
model=ChatHuggingFace(llm=llm)



