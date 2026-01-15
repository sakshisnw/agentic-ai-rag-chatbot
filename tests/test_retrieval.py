from rag.retriever import get_retriever

def test_retriever():
    retriever = get_retriever()
    docs = retriever.invoke("What is Agentic AI?")

    assert docs is not None
    assert len(docs) > 0
