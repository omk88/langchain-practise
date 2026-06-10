from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, ChatOllama 
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def run_chat_interface():
    model = ChatOllama(model="llama3.2:1b")
    
    embeddings = OllamaEmbeddings(model="bge-large")
    
    print("Loading vector store...")
    vector_store = FAISS.load_local(
        "../4. TEXT PROCESSING & DOCUMENT MANAGEMENT/faiss_index", 
        embeddings, 
        allow_dangerous_deserialization=True
    )
    retriever = vector_store.as_retriever(search_kwargs={"k": 2})

    def format_docs(docs):
        return "\n\n".join(d.page_content for d in docs)

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are an expert banking assistant specialized in {banking_division}.\nContext:\n{context}"),
        ("human", "Can you explain {financial_term} like I am 5 years old?")
    ])

    rag_chain = (
        {
            "context": (lambda x: x["financial_term"]) | retriever | format_docs,
            
            "banking_division": lambda x: x["banking_division"],
            "financial_term": lambda x: x["financial_term"]
        }
        | prompt_template
        | model
        | StrOutputParser()
    )

    user_inputs = {
        "banking_division": "Investment Banking and Capital Markets",
        "financial_term": "Liquidity Risk"
    }
    
    print("\nStreaming answer from Ollama...")
    print(rag_chain.invoke(user_inputs))

if __name__ == "__main__":
    run_chat_interface()