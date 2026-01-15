from ingest.loader import load_pdf

def test_pdf_loading():
    docs = load_pdf("Ebook-Agentic-AI.pdf")
    assert docs is not None
    assert len(docs) > 0
