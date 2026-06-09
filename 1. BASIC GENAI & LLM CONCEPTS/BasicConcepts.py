# Basic GenAI concepts


# 1. System vs User Prompts

# When communicating with a chat-optimised model, your inputs are split into distinct architectural "roles".
# The two most vital roles to distinguish are **System** and **User**.

# The system prompt (the persona and guardrails):

# - What it is: High-level architectural instructions that configure the models behaviour, tone, constraints and boundaries.

# The analogy: This is the training or employee handbook you give to an analyst before they start working.

# Example: "You are a compliance officer at Citi. You only speak in a professional tone and must reject any requests to analyse non-financial text."



# 2. The user prompt (the task):

# What it is: The immediate, live request or query provided by the end-user that needs processing.

# The analogy: This is the specific assignment a manager drops on the analysts desk for the day.

# Example: "Analyse this transaction history for suspicious activity."


# TEST TRAP! - A common mistake is cramming background rules into the user prompt. Keep instructions in the system prompt so that the model separates *how* it should behave from *the data it is processing*.

