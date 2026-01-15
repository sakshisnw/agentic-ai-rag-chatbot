import os
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

from config import (
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME,
    EMBEDDING_MODEL
)

def get_retriever():
    # Ensure Pinecone key is available
    os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vectorstore = PineconeVectorStore.from_existing_index(
        index_name=PINECONE_INDEX_NAME,
        embedding=embeddings
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    return retriever
