# 🚀 Generative AI Using LangChain

A practical **Generative AI learning repository** focused on building applications with **LangChain, Ollama, Hugging Face, structured outputs, prompts, chains, output parsers, and Streamlit**.

This repository contains hands-on implementations and examples designed to understand how LangChain works from the fundamentals to practical LLM application development.

---

## 📌 About the Project

**Generative AI Using LangChain** is a collection of practical examples for learning and experimenting with Large Language Models (LLMs) using the LangChain framework.

The repository covers important LangChain concepts including:

* 🧠 LLMs and Chat Models
* ✍️ Prompt Templates
* 🔗 LangChain Chains
* 📤 Output Parsers
* 📦 Structured Outputs
* 🤖 Ollama Integration
* 🤗 Hugging Face Models
* 💬 Streamlit Chatbot
* 📐 JSON Schema
* 🐍 Pydantic Models
* 📋 TypedDict
* 🔢 Embeddings
* 📊 Cosine Similarity

The main goal is to understand how individual LangChain components work and how they can be combined to build real-world Generative AI applications.

---

# 🎯 Learning Objectives

By working through this repository, you will learn how to:

* Understand the fundamentals of LangChain
* Work with different LLM providers
* Use locally hosted models with Ollama
* Create reusable prompt templates
* Build sequential and parallel chains
* Create conditional workflows
* Parse LLM responses into structured formats
* Use Pydantic for structured outputs
* Work with JSON schemas
* Use TypedDict with structured outputs
* Generate embeddings
* Calculate cosine similarity
* Build a chatbot using LangChain
* Integrate LangChain with Streamlit
* Understand the basic architecture of LLM applications

---

# 🛠️ Technologies Used

| Technology      | Purpose                             |
| --------------- | ----------------------------------- |
| 🐍 Python       | Programming Language                |
| 🦜 LangChain    | LLM Application Framework           |
| 🦙 Ollama       | Run LLMs Locally                    |
| 🤗 Hugging Face | Open-source Models                  |
| ⚡ Streamlit     | Web UI                              |
| 🧩 Pydantic     | Data Validation & Structured Output |
| 📋 TypedDict    | Typed Structured Data               |
| 🔢 NumPy        | Numerical Operations                |
| 📊 Scikit-learn | Similarity & ML Utilities           |

---

# 📂 Project Structure

```text
Gen-Ai-Using-Langchain/
│
├── langchain-intro/
│   └── README.md
│
├── langchain-components/
│   └── README.md
│
├── langchain-models/
│   ├── chatmodels.py
│   ├── chatmodel_huggingface.py
│   ├── llms.py
│   ├── embedding_models.py
│   └── cosine-similarity.py
│
├── langchain-prompts/
│   ├── app.py
│   ├── chatbot.py
│   ├── prompt.py
│   └── Langchain_prompt_templates.ipynb
│
├── langchain-chains/
│   ├── simplechain.py
│   ├── sequentialchain.py
│   ├── parallelchain.py
│   └── conditionalchain.py
│
├── langchain-output-parsers/
│   ├── stringoutputparser.py
│   ├── jsonoutputparser.py
│   ├── structuredoutputparser.py
│   └── pydanticparser.py
│
├── langchain-structured-outputs/
│   ├── json_schema.py
│   ├── pydantic.py
│   └── typeddict.py
│
├── requirements.txt
└── README.md
```

---

# 🧠 LangChain Overview

LangChain is a framework for developing applications powered by Large Language Models.

Instead of directly sending a prompt to an LLM, LangChain provides components that allow developers to build more powerful workflows.

A typical LangChain application can be represented as:

```text
User Input
    ↓
Prompt Template
    ↓
LLM / Chat Model
    ↓
Output Parser
    ↓
Structured / Usable Output
```

These components can also be connected together using **LangChain Expression Language (LCEL)**.

Example:

```python
chain = prompt | model | parser
```

---

# 🧩 LangChain Components

The repository explores the major building blocks of LangChain.

## 1. Models

Models are responsible for generating responses or transforming information.

Examples include:

* LLMs
* Chat Models
* Embedding Models

This project demonstrates models from:

* Ollama
* Hugging Face
* Other LLM providers supported by LangChain

---

## 2. Prompts

Prompts define what information or instructions are given to the model.

LangChain provides reusable prompt templates that make it easier to dynamically insert user input.

Example:

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    template="Explain {topic} in simple words.",
    input_variables=["topic"]
)
```

---

## 3. Chains

Chains connect multiple LangChain components together.

For example:

```text
Prompt
   ↓
Model
   ↓
Parser
```

In LCEL:

```python
chain = prompt | model | parser
```

The repository demonstrates:

* Simple Chains
* Sequential Chains
* Parallel Chains
* Conditional Chains

---

# 🔗 Chains Covered

## Simple Chain

A simple chain connects components in a straightforward sequence.

```text
Input
  ↓
Prompt
  ↓
Model
  ↓
Output
```

---

## Sequential Chain

Multiple operations are executed one after another.

```text
Input
  ↓
Chain 1
  ↓
Chain 2
  ↓
Chain 3
  ↓
Final Output
```

Useful when the output of one operation becomes the input for another.

---

## Parallel Chain

Multiple operations can execute independently.

```text
              ┌──→ Chain A ──→ Output A
Input ────────┤
              └──→ Chain B ──→ Output B
```

Useful when multiple pieces of information need to be generated from the same input.

---

## Conditional Chain

A conditional chain selects different processing paths based on a condition.

```text
                 ┌──→ Path A
Input → Condition
                 └──→ Path B
```

This allows applications to implement decision-based workflows.

---

# ✍️ Prompt Engineering

The project also demonstrates how prompts can be separated from application logic.

For example:

```python
prompt = """
You are a helpful, intelligent, and friendly AI assistant.

Answer questions clearly and accurately.
Do not make up information.
If you are uncertain, clearly state that you are uncertain.
"""
```

Keeping prompts separate makes applications:

* Easier to maintain
* Easier to modify
* Easier to test
* More reusable

---

# 📤 Output Parsers

LLMs normally return text.

Output parsers allow developers to transform model responses into useful formats.

This repository explores:

### String Output Parser

```python
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

chain = prompt | model | parser
```

Returns a clean string instead of the complete model response object.

---

### JSON Output Parser

Allows model responses to be converted into JSON-compatible structures.

Useful when applications require machine-readable data.

---

### Structured Output Parser

Allows developers to define expected response fields.

Example structure:

```text
{
    "topic": "...",
    "summary": "...",
    "example": "..."
}
```

This is useful when consistent output is required from an LLM.

---

### Pydantic Output Parser

Pydantic models can define the expected structure and validate the generated response.

Example:

```python
class Person(BaseModel):
    keyword: list[str]
    usage: list[str]
    example: list[str]
    summary: str
```

---

# 📦 Structured Outputs

Structured outputs allow LLMs to return information according to a predefined schema.

This repository demonstrates three approaches.

## JSON Schema

```python
json_schema = {
    "title": "Movie",
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "year": {"type": "integer"},
        "director": {"type": "string"},
        "rating": {"type": "number"}
    },
    "required": [
        "title",
        "year",
        "director",
        "rating"
    ]
}
```

---

## Pydantic

```python
class Data(BaseModel):
    keyword: list[str]
    pros: list[str]
    cons: list[str]
    usage: list[str]
```

The model can then be configured to generate output according to this structure.

---

## TypedDict

TypedDict can also be used to describe the expected structure.

```python
class Data(TypedDict):
    keyword: list[str]
    pros: list[str]
    cons: list[str]
    usage: list[str]
```

---

# 🦙 Ollama Integration

This project primarily uses **Ollama** for running LLMs locally.

Example:

```python
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)
```

This allows experimentation with LLM applications without depending entirely on cloud APIs.

### Example Model

```text
qwen2.5:3b
```

You can replace the model with another model available in your local Ollama installation.

---

# 🤗 Hugging Face Integration

The repository also contains examples demonstrating how LangChain can work with Hugging Face models.

This provides access to a wide ecosystem of open-source models.

---

# 🔢 Embeddings

Embeddings convert text into numerical vectors.

For example:

```text
"Artificial Intelligence"
          ↓
    Embedding Model
          ↓
[0.12, -0.34, 0.81, ...]
```

Embeddings are useful for:

* Semantic search
* Document retrieval
* Recommendation systems
* Similarity comparison
* RAG applications

---

# 📊 Cosine Similarity

Cosine similarity can be used to determine how similar two vectors are.

Conceptually:

```text
Text A → Embedding A
                  \
                   → Cosine Similarity → Similarity Score
                  /
Text B → Embedding B
```

This repository includes an example demonstrating cosine similarity.

---

# 💬 LangChain Chatbot

The project includes both a command-line chatbot and a Streamlit-based chatbot.

The chatbot maintains conversation history using LangChain message objects.

```text
User
 ↓
Conversation History
 ↓
Chat Prompt Template
 ↓
Ollama Chat Model
 ↓
AI Response
 ↓
Updated History
```

---

# 🌐 Streamlit Application

A Streamlit application is included to provide a simple web interface for interacting with the chatbot.

Run the application with:

```bash
streamlit run langchain-prompts/app.py
```

The application provides:

* 🤖 Chat interface
* 💬 Conversation history
* 🦙 Ollama-powered responses
* 🧹 Clear chat functionality

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/Gen-Ai-Using-Langchain.git
```

Navigate into the project:

```bash
cd Gen-Ai-Using-Langchain
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🦙 Setting Up Ollama

Install Ollama on your system and download the model you want to use.

For example:

```bash
ollama pull qwen2.5:3b
```

Verify the model:

```bash
ollama list
```

You should see the downloaded model in the list.

Then make sure Ollama is running before executing the LangChain examples.

---

# ▶️ Running the Examples

Each directory contains independent examples.

### Models

```bash
python langchain-models/chatmodels.py
```

### Prompts

```bash
python langchain-prompts/chatbot.py
```

### Chains

```bash
python langchain-chains/simplechain.py
```

### Output Parsers

```bash
python langchain-output-parsers/stringoutputparser.py
```

### Structured Outputs

```bash
python langchain-structured-outputs/pydantic.py
```

---

# 🌐 Running the Streamlit Chatbot

Start Streamlit using:

```bash
streamlit run langchain-prompts/app.py
```

Then open the local URL displayed in your terminal.

---

# 📋 Requirements

The project uses several Python packages.

Main dependencies include:

```text
langchain
langchain-core
langchain-community
langchain-ollama
langchain-huggingface
transformers
huggingface-hub
pydantic
numpy
scikit-learn
streamlit
python-dotenv
```

Additional integrations are included in `requirements.txt` for providers such as:

* OpenAI
* Anthropic
* Google Generative AI
* Hugging Face
* Ollama

---

# 🏗️ Overall Architecture

A simplified architecture of the project:

```text
                    ┌──────────────────┐
                    │    User Input    │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Prompt Template  │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │   Chat / LLM     │
                    │      Model       │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Output Parser /  │
                    │ Structured Output│
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Final Application│
                    │     Output       │
                    └──────────────────┘
```

---

# 🎓 What You Can Build With These Concepts

Once these concepts are understood, they can be combined to build more advanced Generative AI applications such as:

* 🤖 AI Chatbots
* 📚 RAG Applications
* 🔎 Semantic Search Systems
* 📄 Document Q&A Systems
* 🧠 AI Agents
* 💬 Customer Support Assistants
* 📊 AI Data Analysis Applications
* 📝 AI Content Generation Tools
* 🎯 Recommendation Systems
* 🧾 Document Extraction Systems

---

# 🚀 Future Improvements

Possible extensions for this project include:

* [ ] Add RAG implementation
* [ ] Add vector databases
* [ ] Add document loaders
* [ ] Add text splitters
* [ ] Add retrievers
* [ ] Build an AI agent
* [ ] Add tool calling
* [ ] Add conversational memory
* [ ] Add multiple Ollama model selection
* [ ] Add streaming responses
* [ ] Add LangSmith tracing
* [ ] Deploy the Streamlit application
* [ ] Add automated tests
* [ ] Add more real-world GenAI projects

---

# 📚 Learning Path

A recommended learning order for this repository:

```text
1. LangChain Introduction
          ↓
2. LangChain Components
          ↓
3. Models
          ↓
4. Prompt Templates
          ↓
5. Chains
          ↓
6. Output Parsers
          ↓
7. Structured Outputs
          ↓
8. Embeddings
          ↓
9. Chatbots
          ↓
10. RAG
          ↓
11. Agents
          ↓
12. Production GenAI Applications
```

---

# 💡 Key Takeaways

Through this project, you will understand how LangChain acts as a bridge between application logic and Large Language Models.

The most important concepts are:

```text
Models
   +
Prompts
   +
Chains
   +
Output Parsers
   +
Structured Outputs
   =
Powerful LLM Applications
```

LangChain becomes especially useful when an application needs more than a simple prompt-and-response interaction.

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you would like to contribute:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push the branch
6. Open a Pull Request

---

# ⭐ Support

If you find this repository useful for learning Generative AI and LangChain, consider giving it a ⭐ on GitHub.

---

## 👨‍💻 Author

**Jilla Srivardhan**

Exploring:

```text
Python → Machine Learning → Generative AI → LangChain → LLM Applications
```

---

## 📄 License

This project is intended primarily for **learning, experimentation, and educational purposes**.

You are free to use and modify the examples for your own learning and projects.
