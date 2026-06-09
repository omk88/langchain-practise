from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="llama3.2:1b")

prompt = ChatPromptTemplate.from_messages ([
    ("system", "You are a senior finacial auditor at Citi. Keep definitions brief."),
    ("human", "Explain what {financial_concept} means.")
])

parser = StrOutputParser()

chain = prompt | model | parser

print("Executing the LCEL chain pipeline...")

result = chain.invoke({"financial_concept": "Market Volatility"})

print("\n --- Clean Processed Output ---")

print(result)

print("\n--- EXAM FOCUS: Verifying Return Data Type ---")
print(f"The resulting data type is: {type(result).__name__}")
