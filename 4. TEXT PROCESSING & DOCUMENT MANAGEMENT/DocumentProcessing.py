import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

def build_and_save_vector_store():
    file_path = os.path.join("data", "citi_policy.txt")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Please place your text file at: {file_path}")

    print(f"Loading document from {file_path}...")
    loader = TextLoader(file_path)
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=120, chunk_overlap=20)
    chunks = text_splitter.split_documents(documents)
    print(f"Split document into {len(chunks)} chunks.")
    
    print("Generating embeddings via Ollama...")
    embeddings = OllamaEmbeddings(model="bge-large")
    
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local("faiss_index")
    print("Success! 'faiss_index' folder created via Ollama Embeddings.")

if __name__ == "__main__":
    build_and_save_vector_store()