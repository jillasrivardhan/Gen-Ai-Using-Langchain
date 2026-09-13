
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

from dotenv import load_dotenv

load_dotenv()

model = HuggingFaceEndpoint(
   repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
   task = "text-generation"
)

chatmodel = ChatHuggingFace(
   llm = model
)

response = chatmodel.invoke("what is the capital of india?")

print(response.content)