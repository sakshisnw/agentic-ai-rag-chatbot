from ingest.loader import load_pdf
from ingest.chunker import chunk_documents

def test_chunking():
    docs = load_pdf("Ebook-Agentic-AI.pdf")
    chunks = chunk_documents(docs)

    assert chunks is not None
    assert len(chunks) > len(docs)
