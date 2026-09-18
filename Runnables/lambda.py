
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough,RunnableLambda
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


def counter(text):
   return len(text.split())

word_counter = RunnableLambda(counter)

model = ChatOllama(
   model='qwen2.5:3b'
)

prompt = PromptTemplate(
   template="generate 3 simple key points on the {topic}",
   input_variables=['topic']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt,model,parser)

parallel = RunnableParallel({
   'passthrough':RunnablePassthrough(),
   'count':RunnableLambda(counter)
})

final = RunnableSequence(chain,parallel)

response = final.invoke({'topic':'football'})

print('-'*20)
print(response['passthrough'])
print('-'*20)
print(response['count'])