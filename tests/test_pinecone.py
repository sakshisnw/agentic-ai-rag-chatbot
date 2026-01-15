from ingest.loader import load_pdf
from ingest.chunker import chunk_documents
from ingest.embed_store import ingest_to_pinecone

def test_pinecone_ingestion():
    docs = load_pdf("Ebook-Agentic-AI.pdf")
    chunks = chunk_documents(docs)

    ingest_to_pinecone(chunks)

    # If no exception is raised, test passes
    assert True
