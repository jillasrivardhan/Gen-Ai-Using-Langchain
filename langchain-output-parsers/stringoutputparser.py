
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# model = ChatOllama(
#    model="qwen2.5:3b",
#    temperature=0
# )

# prompt = PromptTemplate(
#    template="explain about {topic} in 3 simple points",
#    input_variables=["topic"]
# )

# parser = StrOutputParser()

# response = prompt.invoke({'topic':'ai'})

# message = model.invoke(response)

# result = parser.parse(message)


# # print(result)
# print(result.content)


#==========================
# USING CHAINS
#==========================

model = ChatOllama(
   model="qwen2.5:3b",
   temperature=0
)

prompt = PromptTemplate(
   template="explain about {topic} in 3 simple points",
   input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({'topic':'ai'})

print(response)



