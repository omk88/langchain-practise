from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.embeddings import FakeEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain_community.llms import FakeListLLM
from langchain_text_splitters import RecursiveCharacterTextSplitter

# --- 1. THE DATA SOURCE ---
# In a real app, this might be a PDF, text file, or webpage.
raw_documents = [
    Document(
        page_content="The secret ingredient to the ultimate pizza dough is a 72-hour cold fermentation. This develops deep flavor and a bubbly crust.",
        metadata={"source": "pizza_secrets.txt"}
    ),
    Document(
        page_content="Pineapple on pizza was invented in Canada in 1962 by Sam Panopoulos at the Satellite Restaurant.",
        metadata={"source": "pizza_history.txt"}
    )
]

# --- 2. CHUNKING & EMBEDDINGS ---
# Split documents into smaller, digestible chunks for the vector store
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
docs = text_splitter.split_documents(raw_documents)

# Create a mock embedding model (size 10 matches our fake vector dimensions)
embeddings = FakeEmbeddings(size=10)

# Load the chunks into a local in-memory FAISS vector store
vector_store = FAISS.from_documents(docs, embeddings)

# Turn the vector store into a retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 1})


# --- 3. THE MOCK LLM & PROMPT ---
# We define what the fake LLM will "respond" with when called
fake_responses = ["Based on the provided context, the secret ingredient is a 72-hour cold fermentation which develops deep flavor."]
llm = FakeListLLM(responses=fake_responses)

# Define the RAG prompt template
prompt_template = """You are a helpful assistant. Answer the question using only the following context:

Context: {context}

Question: {question}
Answer:"""
prompt = ChatPromptTemplate.from_template(prompt_template)


# --- 4. THE RAG CHAIN ---
# Helper function to format retrieved documents for the prompt
def format_docs(retrieved_docs):
    return "\n\n".join(doc.page_content for doc in retrieved_docs)

# Constructing the pipeline using LangChain Expression Language (LCEL)
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# --- 5. EXECUTION ---
query = "What makes the best pizza dough?"
print(f"User Query: {query}\n")

# Run the chain
response = rag_chain.invoke(query)
print(f"Pipeline Response:\n{response}")