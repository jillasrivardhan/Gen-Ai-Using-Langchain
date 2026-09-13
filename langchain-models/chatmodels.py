from langchain_ollama import ChatOllama

chatmodel = ChatOllama(
   model = "qwen2.5:3b",
   temperature = 0,
   max_completion_tokens = 5
)

chatmodel_response = chatmodel.invoke("Explain about india.")

# print(chatmodel_response)

print(chatmodel_response.content)