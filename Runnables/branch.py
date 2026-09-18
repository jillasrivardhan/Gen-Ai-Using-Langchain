from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough,RunnableBranch,RunnableLambda
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(
   model='qwen2.5:3b',
   temperature=0
)

prompt_1 = PromptTemplate(
   template="explain about the {topic}",
   input_variables=['topic']
)

prompt_2 = PromptTemplate(
   template="summarize the following text \n {text}",
   input_variables=['text']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt_1,model,parser)

branch = RunnableBranch(
   (
      lambda X: len(X.split()) > 300,
      RunnableSequence(prompt_2,model,parser)
   ),

   RunnablePassthrough()
)

final = RunnableSequence(chain,branch)

response = final.invoke({
   'topic':'hockey'
})

print(response)
print('-'*20)
print(len(response.split()))


