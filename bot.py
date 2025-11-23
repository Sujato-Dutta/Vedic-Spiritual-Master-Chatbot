import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

load_dotenv()

DB_PATH = "chroma_db"

def get_rag_chain():
    # 1. Setup Vector DB
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Chroma DB not found at {DB_PATH}. Please run ingest_data.py first.")
        
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    vector_db = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})

    # 2. Setup LLM
    llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", temperature=0.7)

    # 3. Setup Prompt
    template = """You are a wise Spiritual Master, deeply versed in the Vedas, Upanishads, Bhagavad Gita, and Yoga Vashishta.
    Your goal is to provide guidance to modern individuals facing daily life problems, using the wisdom of these ancient texts.
    
    Use the following pieces of context to answer the question at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Always quote relevant verses or concepts from the texts if possible.
    Keep your tone compassionate, calm, and profound.

    Context: {context}

    Question: {question}

    Spiritual Guidance:"""
    
    prompt = PromptTemplate(
        template=template, 
        input_variables=["context", "question"]
    )

    # 4. Setup Chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )
    
    return qa_chain

if __name__ == "__main__":
    # Test
    try:
        chain = get_rag_chain()
        res = chain.invoke({"query": "I am feeling stressed about my job."})
        print(res["result"])
    except Exception as e:
        print(f"Error: {e}")
