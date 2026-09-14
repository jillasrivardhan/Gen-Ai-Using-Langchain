
from typing import TypedDict, Annotated,Optional,Literal
from langchain_ollama import ChatOllama

model = ChatOllama(model="qwen2.5:3b")

class data(TypedDict):
      keyword:Annotated[list[str],"retrieve the important keywords"]
      pros:Optional[Annotated[list[str],"list the pros of the topic"]]
      cons:Optional[Annotated[list[str],"list the cons of the topic"]]
      usage:Annotated[list[str],"where it is used"]
     

structure = model.with_structured_output(data)

# output = structure.invoke("name: John Doe, age: 30, gender: male")

output = structure.invoke("""
Artificial intelligence (AI) is the capability of computational systems to perform tasks typically associated with human intelligence, such as learning, reasoning, problem-solving, perception, and decision-making.  It is a branch of computer science that uses algorithms and vast amounts of data to mimic human cognitive functions, allowing machines to analyze information, recognize patterns, and act intelligently to achieve specific goals without being explicitly programmed for every scenario. 

AI systems operate by combining data, algorithms, and computational power to identify relationships and make predictions.  This process involves training models on large datasets to recognize patterns, which allows the system to learn from experience and improve its performance over time.  Key technologies within this broad field include machine learning, where systems adapt to new data, and deep learning, which uses neural networks inspired by the human brain to handle complex tasks like image recognition and natural language processing. 

Common applications of AI are deeply integrated into daily life and various industries, including healthcare, finance, transportation, and customer service.  Examples include virtual assistants like Siri and Alexa, recommendation systems on streaming platforms, autonomous vehicles, and generative AI tools that create text, images, or code.  While current AI is often "narrow," designed for specific tasks, research continues into Artificial General Intelligence (AGI), a theoretical future state where systems would possess human-like cognitive flexibility across a wide range of domains.""")


# print(output['keyword'])
print(output['usage'])
# print(output['cons'])