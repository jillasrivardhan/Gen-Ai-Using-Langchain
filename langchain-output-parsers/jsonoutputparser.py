
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# model = ChatOllama(
#    model="qwen2.5:3b",
#    temperature=0
# )

# parser = JsonOutputParser()

# prompt = PromptTemplate(
#    template="explain about {topic} in simple words \n {format_instructions}",
#    input_variables=[],
#    partial_variables={'format_instructions':parser.get_format_instructions()}
# )

# message = prompt.invoke({'topic':'ai'})

# response = model.invoke(message)

# print(response.content)


#============================
# USING CHAINS
#============================

model = ChatOllama(
   model="qwen2.5:3b",
   temperature=0
)

parser = JsonOutputParser()

prompt = PromptTemplate(
   template="explain about {topic} in simple words \n {format_instructions}",
   input_variables=[],
   partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain = prompt | model | parser

response = chain.invoke({'topic':'ai'})

print(response)

