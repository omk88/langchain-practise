from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(model="llama3.2:1b")

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert banking assistant specialized in {banking_division}."),
    ("human", "Can you explain {financial_term} like I am 5 years old?")
])

user_inputs = {
    "banking_division": "Investment Banking and Capital Markets",
    "financial_term": "Liquidity Risk"
}

formatted_messages = prompt_template.format_messages(**user_inputs)

print("--- EXAM FOCUS: Inspecting the Generated Message List ---")
for msg in formatted_messages:
    print(f"Role Class: {type(msg).__name__} | Text: {msg.content}")
print("-" * 60)

print("\nInvoking model with compiled prompt template...")
response = model.invoke(formatted_messages)

print("\n --- Model Response ---")
print(response.content)