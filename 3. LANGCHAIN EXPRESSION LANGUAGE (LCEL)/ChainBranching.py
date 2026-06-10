from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnablePassthrough, RunnableParallel

model = ChatOllama(model="llama3.2:1b")

math_chain = ChatPromptTemplate.from_template("You are a math tutor. Solve this: {query}") | model | StrOutputParser()
general_chain = ChatPromptTemplate.from_template("You are a concierge. Answer this: {query}") | model | StrOutputParser()

classifier_prompt = ChatPromptTemplate.from_template(
    "Classify the user intent into exactly one word: 'math' or 'general'. Query: {query}"
)

classifier_chain = classifier_prompt | model | StrOutputParser()

branching_router = RunnableBranch( 
    (lambda x: "math" in x["intent"].lower(), math_chain),
    general_chain
)

full_routing_pipeline = (
    RunnableParallel({
        "intent": classifier_chain,
        "query": RunnablePassthrough()
    })
    | branching_router
)

print("Testing Routing Pipeline with Math Input...")
print(full_routing_pipeline.invoke({"query": "What is the square root of 144?"}))