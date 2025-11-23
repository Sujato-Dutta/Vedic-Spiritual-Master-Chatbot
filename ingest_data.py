import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

DATA_PATH = "data"
DB_PATH = "chroma_db"

def ingest_data():
    if not os.path.exists(DATA_PATH):
        print(f"Data directory {DATA_PATH} not found.")
        return

    # Load documents
    print("Loading documents...")
    loader = DirectoryLoader(DATA_PATH, glob="*.txt", loader_cls=TextLoader, loader_kwargs={'encoding': 'utf-8'})
    documents = loader.load()
    print(f"Loaded {len(documents)} documents.")

    # Split documents
    print("Splitting documents...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks.")

    # Create embeddings and vector store
    print("Creating vector store...")
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY not found in environment variables.")
        return

    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_PATH
    )
    print(f"Vector store created at {DB_PATH}")

if __name__ == "__main__":
    ingest_data()
