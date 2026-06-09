from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatOllama(model="llama3.2:1b")

messages = [
    SystemMessage(content="You are a funny comedian."),
    HumanMessage(content="Tell me a funny joke."),
    AIMessage(content="What do you call a pig that does karate? A pork chop."),
    HumanMessage(content="Hahahahaha. Tell me another.")
]

print("Sending message array directly to local Ollama...")

response = model.invoke(messages)

print("\n--- Raw Response Object ---")
print(response)

print("\n--- Clean Content Output ---")
print(response.content)