from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch


# --------------------------------------------------
# 1. LLM
# --------------------------------------------------

llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0.7
)

# ---------------------------------------------------
# Parser
# ---------------------------------------------------

parser = StrOutputParser()

# --------------------------------------------------
# 2. Summary Chain
# --------------------------------------------------

summary_prompt = PromptTemplate(
    template="""
    generate a sentiment for the review.

    Topic: {topic}

    """,
    input_variables=["topic"]
)

summary_chain = summary_prompt | llm | parser


# --------------------------------------------------
# 3. Short Explanation Chain
# --------------------------------------------------

positive_prompt = PromptTemplate(
    template="""
   give some keywords that tell it is positive.

    Topic:
    {topic}

    Give a short explanation suitable for a beginner.
    """,
    input_variables=["topic"]
)

positive_chain = positive_prompt | llm | parser


# --------------------------------------------------
# 4. Detailed Explanation Chain
# --------------------------------------------------

negative_prompt = PromptTemplate(
    template="""
    Explain that why it is negative.

    Topic:
    {topic}

    """,
    input_variables=["topic"]
)

negative_chain = negative_prompt | llm | parser


# --------------------------------------------------
# 5. Conditional Chain
# --------------------------------------------------

conditional_chain = RunnableBranch(
    
    # Condition
    (
        lambda x: x["topic"]=='positive',
        positive_chain
    ),

    # Default condition
    negative_chain
)


# --------------------------------------------------
# 6. Run the Chain
# --------------------------------------------------

topic = input("Enter a topic: ")

result = conditional_chain.invoke({
    "topic": topic
})


# --------------------------------------------------
# 7. Display Result
# --------------------------------------------------

print("\n" + "=" * 50)
print("           📚 RESULT")
print("=" * 50)

print(result)

print("=" * 50)