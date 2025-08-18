from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
import os

class TextProcessor:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        # Using local embeddings
        self.embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'}  # Use 'cuda' if you have GPU
        )
        self.vector_store = None

    def chunk_text(self, text: str) -> List[str]:
        """Split text into manageable chunks"""
        return self.text_splitter.split_text(text)

    # def create_vector_store(self, chunks: List[str]) -> None:
    #     """Create vector store from text chunks"""
    #     self.vector_store = Chroma.from_texts(
    #         texts=chunks,
    #         embedding=self.embeddings,
    #         persist_directory="./chroma_db"
    #     )
    def create_vector_store(self, chunks: List[str]) -> None:
        
        try:
            self.vector_store = Chroma.from_texts(
                texts=chunks,
                embedding=self.embeddings,
                persist_directory="./chroma_db"
            )
            print("Vector store created successfully")  # Debug
            return True
        except Exception as e:
            print(f"Error creating vector store: {e}")
            return False
        
    def load_vector_store(self) -> bool:
        try:
            self.vector_store = Chroma(
                persist_directory=self.persist_dir,
                embedding_function=self.embeddings
            )
            return True
        except:
            return False

    # def search_documents(self, query: str, k: int = 3) -> List[str]:
    #     """Search for relevant document chunks"""
    #     if not self.vector_store:
    #         raise ValueError("Vector store not initialized")
    #     docs = self.vector_store.similarity_search(query, k=k)
    #     return [doc.page_content for doc in docs]
    
    def search_documents(self, query: str, k: int = 3) -> List[str]:
        if not self.vector_store and not self.load_vector_store():
            raise ValueError("Vector store not initialized")
        docs = self.vector_store.similarity_search(query, k=k)
        return [doc.page_content for doc in docs]