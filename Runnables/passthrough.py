

from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(
   model='qwen2.5:3b'
)

prompt = PromptTemplate(
   template="generate 3 simple key points on the {topic}",
   input_variables=['topic']
)

uses = PromptTemplate(
   template="explain where it is used mostly {text}",
   input_variables=['text']
)

parser = StrOutputParser()

chain = prompt | model | parser

parallel = RunnableParallel({
   'keypoints':RunnablePassthrough(),
   'uses':RunnableSequence(uses,model,parser)
})

final = RunnableSequence(chain,parallel)

res = final.invoke({'topic':'cricket'})


print('-'*20)
print(res['keypoints'])
print('-'*20)
print(res['uses'])