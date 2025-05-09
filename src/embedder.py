from src.loader import documents
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = OllamaEmbeddings(model="mxbai-embed-large")
vectors = FAISS.from_documents(documents=documents, embedding=embeddings)
