from bot import get_rag_chain
import traceback

try:
    print("Initializing chain...")
    chain = get_rag_chain()
    print("Chain initialized. Invoking...")
    response = chain.invoke({"query": "What is the nature of the self?"})
    print("Response received:")
    print(response)
except Exception:
    traceback.print_exc()
