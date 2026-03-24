import os
from dotenv import load_dotenv
from rag_engine import RAGSystem

load_dotenv()

def test():
    api_key = os.getenv("PINECONE_API_KEY")
    index_name = os.getenv("PINECONE_INDEX_NAME")
    
    print(f"Testing RAG with Index: {index_name}")
    rag = RAGSystem(api_key, index_name)
    
    # Check if we can connect
    if rag.load_index():
        print("Successfully connected to Pinecone.")
        
        query = "Phòng cháy chữa cháy" # Thay đổi query tùy dự án
        print(f"Searching for: {query}")
        
        results = rag.retrieve(query, k=5)
        print(f"Found {len(results)} chunks.")
        for i, res in enumerate(results):
            print(f"--- Chunk {i+1} ---")
            print(f"Source: {res.metadata.get('source')}")
            print(f"Content snippet: {res.page_content[:100]}...")
    else:
        print("Failed to connect to index. Check PINECONE_INDEX_NAME or API KEY.")

if __name__ == "__main__":
    test()
