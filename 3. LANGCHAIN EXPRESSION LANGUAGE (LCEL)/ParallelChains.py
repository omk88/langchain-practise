from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

model = ChatOllama(model="llama3.2:1b")

prompt_compliance = ChatPromptTemplate.from_template("Analyse this financial action for regulatory risk: {action}")
chain_compliance = prompt_compliance | model | StrOutputParser()

prompt_summary = ChatPromptTemplate.from_template("Write a one-sentence high level summary of this action: {action}")
chain_summary = prompt_summary | model | StrOutputParser()

optimised_pipeline = RunnableParallel({
    "regulatory_report": chain_compliance,
    "executive_summary": chain_summary
})

print("Running parallel tracks concurrently...")
final_output = optimised_pipeline.invoke({"action": "Moving $50M to offshore liquidity reserves."})

print("\n--- Output Object Keys ---")
print(final_output.keys())

print("\n--- Regulatory Report ---")
print(final_output["regulatory_report"])

print("\n--- Summary ---")
print(final_output["executive_summary"])

