from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.language_models.fake import FakeListLLM

# 1. Initialize a Mock LLM that returns a pre-defined list of answers
fake_model = FakeListLLM(responses=["The capital of France is Paris."])

# 2. Build a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful geography quiz assistant."),
    ("human", "What is the capital of {country}?")
])

# 3. Use an Output Parser
parser = StrOutputParser()

# 4. Construct the LCEL Chain
chain = prompt | fake_model | parser

# 5. Execute the pipeline
response = chain.invoke({"country": "France"})

print(response)