from langchain_ollama import ChatOllama
from langchain_classic.chains import LLMChain
from langchain_core.prompts import PromptTemplate

model = ChatOllama(
   model = "qwen2.5:3b",
   temperature=0.5
)

prompt = PromptTemplate(
   template="explain about this {topic} in simple words",
   input_variables=['topic']
)

model = LLMChain(llm=model, prompt=prompt)

res = model.invoke({'topic':'ai'})

print(res['text'])