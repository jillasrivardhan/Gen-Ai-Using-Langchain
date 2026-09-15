
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatOllama(model="qwen2.5:3b",temperature=0.5)

prompt = PromptTemplate(
   template="tell me about {topic} in simple words",
   input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({'topic':'gpt-6 astra'})

print(response)
