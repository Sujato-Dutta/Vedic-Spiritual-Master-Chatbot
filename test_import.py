try:
    from langchain.chains import RetrievalQA
    print("Import successful")
except ImportError as e:
    print(f"Import failed: {e}")
    import langchain
    print(f"Langchain version: {langchain.__version__}")
