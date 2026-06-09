# Basic GenAI concepts


# 1. System vs User Prompts

# When communicating with a chat-optimised model, your inputs are split into distinct architectural "roles".
# The two most vital roles to distinguish are **System** and **User**.

# The system prompt (the persona and guardrails):
# - What it is: High-level architectural instructions that configure the models behaviour, tone, constraints and boundaries.
# The analogy: This is the training or employee handbook you give to an analyst before they start working.
# Example: "You are a compliance officer at Citi. You only speak in a professional tone and must reject any requests to analyse non-financial text."

# The user prompt (the task):
# What it is: The immediate, live request or query provided by the end-user that needs processing.
# The analogy: This is the specific assignment a manager drops on the analysts desk for the day.
# Example: "Analyse this transaction history for suspicious activity."

# TEST TRAP! - A common mistake is cramming background rules into the user prompt. Keep instructions in the system prompt so that the model separates *how* it should behave from *the data it is processing*.



# 2. Tokens (How text length is measured by models)

# LLMs do not read text character-by-character, nor do they read word-by-word. They process text in structural fragments called **Tokens**.
# What is a token? A token can be a single character, a syllable, a whole common word, or a piece of a word.
# (E. g., the word "LangChain" might be split by a model into two tokens. ["Lang", "Chain"]).

# The rough rule of thumb: On average, 1 token is approximately 4 characters or roughly 0.75 words in English.
# Why it matters for your code:
#   - Context windows: Every model has a hard token limit (e. g. Llama 3.2 1B has a limit of 128,000 tokens). If your RAG pipeline fetches too much context, your script will crash with a context overflow error.
#   - Cost/latency: More tokens mean more math operations, which means your code runs slower.