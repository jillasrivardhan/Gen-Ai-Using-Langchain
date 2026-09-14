
from langchain_core.output_parsers import PydanticOutputParser
from langchain_ollama import ChatOllama
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate

# model = ChatOllama(
#    model="qwen2.5:3b"
# )


# class person(BaseModel):
#    keyword : list[str] = Field(description="important keywords")
#    usage : list[str] = Field(description="where can we use it")
#    example : list[str] = Field(description="in simple words about it")
#    summary:str = Field(description='short 3 lines about it')

# parser = PydanticOutputParser(pydantic_object=person)


# prompt = PromptTemplate(
#    template="explain about {topic} for a 5 year old kid \n {format_instructions}",
#    input_variables=['topic'],
#    partial_variables={'format_instructions':parser.get_format_instructions()}
# )

# message = prompt.invoke({'topic':'ai'})

# response = model.invoke(message)

# result = parser.parse(response.content)

# print(result)



#=================================  
# USING CHAINS
#=================================

model = ChatOllama(
   model="qwen2.5:3b"
)


class person(BaseModel):
   keyword : list[str] = Field(description="important keywords")
   usage : list[str] = Field(description="where can we use it")
   example : list[str] = Field(description="in simple words about it")
   summary:str = Field(description='short 3 lines about it')

parser = PydanticOutputParser(pydantic_object=person)


prompt = PromptTemplate(
   template="explain about {topic} for a 5 year old kid \n {format_instructions}",
   input_variables=['topic'],
   partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain = prompt | model | parser

result = chain.invoke({'topic':'ai'})

print(result)
# print(result['summary'])