

from langchain_core.runnables import RunnableParallel,RunnableSequence
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(
   model='qwen2.5:3b'
)

summary = PromptTemplate(
   template="generate a 20 words summary on {topic}",
   input_variables=['topic']
)

linkedin_post = PromptTemplate(
   template="generate a linkedin post on {topic}",
   input_variables=['topic']
)

parser = StrOutputParser()

chain = RunnableParallel({
   'linkedin-post': RunnableSequence(linkedin_post,model,parser),
   'summary':RunnableSequence(summary,model,parser)
})

response = chain.invoke({'topic':'tool-calling'})

print('-'* 20)
print(response['linkedin-post'])
print('-'* 20)
print(response['summary'])
