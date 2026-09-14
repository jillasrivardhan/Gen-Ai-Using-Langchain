
import streamlit as st

from langchain_ollama import ChatOllama
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from prompt import prompt


# =====================================
# Streamlit Page Configuration
# =====================================

st.set_page_config(
    page_title="LangChain Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 LangChain Chatbot")
st.caption("Powered by Ollama + LangChain")


# =====================================
# Loading the model
# =====================================

chatmodel = ChatOllama(
    model="qwen2.5:3b",
    temperature=0,
    max_completion_tokens=5
)


# =====================================
# Starting the conversation
# =====================================

if "history" not in st.session_state:
    st.session_state.history = []


history = st.session_state.history


# =====================================
# ChatPrompt Template
# =====================================

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", prompt),
        MessagesPlaceholder(variable_name="history")
    ]
)


# =====================================
# Display conversation history
# =====================================

for message in history:

    if isinstance(message, HumanMessage):

        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):
            st.write(message.content)


# =====================================
# User Input
# =====================================

user_input = st.chat_input("Ask me anything...")


# =====================================
# Running the chatbot
# =====================================

if user_input:

    # Display user's message
    with st.chat_message("user"):
        st.write(user_input)

    # Add user message to history
    history.append(
        HumanMessage(content=user_input)
    )

    # Create chain
    chain = prompt | chatmodel

    # Get response from AI
    chatmodel_response = chain.invoke(
        {
            "history": history,
            "input": user_input
        }
    )

    # Add AI response to history
    history.append(
        AIMessage(content=chatmodel_response.content)
    )

    # Display AI response
    with st.chat_message("assistant"):
        st.write(chatmodel_response.content)


# =====================================
# Clear Chat
# =====================================

if st.sidebar.button("Clear Chat"):

    st.session_state.history = []

    st.rerun()

