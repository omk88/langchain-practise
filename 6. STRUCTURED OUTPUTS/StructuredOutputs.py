from typing import List, Optional
from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

class FinancialRiskProfile(BaseModel):
    risk_level: str = Field(description="Must be exactly one of these: 'High', 'Medium' or 'Low'")
    credit_score_estimate: int = Field(description="An estimated numerical credit score between 300 and 850.")
    red_flags: List[str] = Field(description="A list of any concerning warning flags found in the text.")
    approved: bool = Field(description="Set to True if risk is Low or Medium, otherwise False.")
    secondary_notes: Optional[str] = Field(description="Any extra contextual analysis, if applicable.")

model = ChatOllama(model="llama3.2:1b")

structured_model = model.with_structured_output(FinancialRiskProfile)

prompt = ChatPromptTemplate.from_template(
    "Analyse the following applicant text and extract their risk profile:\n\n{applicant_text}"
)

chain = prompt | structured_model

raw_text = """
Applicant has an active mortgage with zero missed payments over 5 years. 
However, their recent credit report shows a new hard inquiry from a high-interest payday loan lender 
and a maxed out credit card statement balance. Overall background checking looks stable but showing signs of recent stress.
"""

print("Running structured extraction...")

result = chain.invoke({"applicant_text": raw_text})

print("\n--- EXAM FOCUS: Verifying the Output Object ---")
print(f"Returned object type: {type(result).__name__}\n")

print(f"Risk Level Assessed: {result.risk_level}")
print(f"Estimated Credit Score: {result.credit_score_estimate}")
print(f"Red Flags Detected: {result.red_flags}")
print(f"System Auto-Approved: {result.approved}")