from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


model = ChatOllama(
   model = "qwen2.5:3b",
   temperature=0.5
)

prompt = PromptTemplate(
   template="explain about this {topic} in simple words",
   input_variables=['topic']
)

topic = input("enter a topic: ")

message = prompt.format(topic= topic)

response = model.invoke(message)

print(response.content)


