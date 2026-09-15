
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


parser = StrOutputParser()

#========================
#summary on topic
#========================

model = ChatOllama(model="qwen2.5:3b",temperature=0.5)

summary_prompt = PromptTemplate(
   template="generate a short summary on {topic}",
   input_variables=['topic']
)

summary_chain = summary_prompt | model | parser


# --------------------------------------------------
# 3. Keyword Chain
# --------------------------------------------------

keyword_prompt = PromptTemplate(
    template="""
    Based on the following summary, generate 5 important keywords.

    Summary:
    {summary}

    Return only the keywords as a numbered list.
    """,
    input_variables=["summary"]
)

keyword_chain = keyword_prompt | model | parser


# --------------------------------------------------
# 4. Quiz Chain
# --------------------------------------------------

quiz_prompt = PromptTemplate(
    template="""
    Based on the following summary, generate 5 multiple-choice
    quiz questions.

    Summary:
    {summary}

    For each question provide:
    - Question
    - A
    - B
    - C
    - D
    - Correct Answer

    Keep the questions simple and beginner-friendly.
    """,
    input_variables=["summary"]
)

quiz_chain = quiz_prompt | model | parser

parallel_chain = RunnableParallel(
    keywords=keyword_chain,
    quiz=quiz_chain
)

full_chain = summary_chain | parallel_chain

result = full_chain.invoke({
    "topic": 'ai'
})

print("*"*20)
print(summary_chain.invoke({'topic':'ai'}))
print("*"*20)

print("keywords: ",result['keywords'])
print("*"*20)


print("quiz: ",result['quiz'])
print("*"*20)

# print(parallel_chain.get_graph().print_ascii())