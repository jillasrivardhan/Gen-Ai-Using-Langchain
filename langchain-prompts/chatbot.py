
from langchain_ollama import ChatOllama
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from prompt import prompt


#=====================================
# loading the model
#=====================================

chatmodel = ChatOllama(
   model = "qwen2.5:3b",
   temperature = 0,
   max_completion_tokens = 5
)

#====================================
# starting the conversation
#====================================

history = []

#====================================
# chatprompt template
#===================================

prompt = ChatPromptTemplate.from_messages(
   [
      ('system', prompt), # takes the system prompt from the prompt.py file
      MessagesPlaceholder(variable_name="history") # takes the conversation history
      
   ]
)

#====================================
# running the chatbot loop
#====================================

while True:
   user_input = input("You:  ")

   chain = prompt | chatmodel # create a chain that combines the prompt and the chat model

   history.append(HumanMessage(content=user_input))

   if user_input.lower() == "exit":
      break

   chatmodel_response = chain.invoke({"history": history, "input": user_input}) # store the response from the chat model in a variable


   history.append(AIMessage(content=chatmodel_response.content))

   print("AI: ", chatmodel_response.content)

# the history variable is a list that stores the conversation history between the user and the AI assistant. 
# Each time the user inputs a message, it is appended to the history as a HumanMessage, and the AI's response is appended as an AIMessage. 
# This allows the chatbot to maintain context and provide more relevant responses based on the ongoing conversation.

print(history)
