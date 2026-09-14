
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

model = ChatOllama(
   model="qwen2.5:3b",
   temperature=0
)


# --------------------------------------------------
# Define Output Schema
# --------------------------------------------------

response_schemas = [
    ResponseSchema(
        name="topic",
        description="The topic being explained"
    ),
    ResponseSchema(
        name="summary",
        description="A short summary of the topic"
    ),
    ResponseSchema(
        name="example",
        description="A simple example of the topic"
    )
]

# --------------------------------------------------
# Create Output Parser
# --------------------------------------------------

output_parser = StructuredOutputParser.from_response_schemas(
    response_schemas
)

# Get formatting instructions
format_instructions = output_parser.get_format_instructions()

# --------------------------------------------------
# Prompt
# --------------------------------------------------

prompt = PromptTemplate(
    template="""
Explain the following topic:

{topic}

{format_instructions}
""",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": format_instructions
    }
)

# --------------------------------------------------
# Chain
# --------------------------------------------------

chain = prompt | model | output_parser

# --------------------------------------------------
# Invoke
# --------------------------------------------------

final = chain.invoke({
    "topic": "Artificial Intelligence"
})

print(final)
