from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

# Connects automatically to the background service running on your PC
model = ChatOllama(model="llama3.2:1b")

messages = [
    SystemMessage(content="You are a strict, no-nonsense financial analyst."),
    HumanMessage(content="What is liquidity risk?")
]

response = model.invoke(messages)
print(response.content)