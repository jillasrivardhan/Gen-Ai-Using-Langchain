

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatOllama(model="qwen2.5:3b",temperature=0.5)

prompt_1 = PromptTemplate(
   template="tell me about {topic} in simple words",
   input_variables=['topic']
)

prompt_2 = PromptTemplate(
   template="list out where it is used mostly\n {text}",
   input_variables=['text']
)

parser = StrOutputParser()

chain = prompt_1 | model | parser | prompt_2 | model | parser

response = chain.invoke({'topic':'ai'})

print(response)