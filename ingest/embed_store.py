import os
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

from config import (
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME,
    EMBEDDING_MODEL
)

def ingest_to_pinecone(chunks):
    os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    # LangChain handles index connection internally
    PineconeVectorStore.from_documents(
        chunks,
        embeddings,
        index_name=PINECONE_INDEX_NAME
    )
