from rag.graph import build_graph

def test_rag_graph():
    graph = build_graph()

    result = graph.invoke({
        "question": "What is Agentic AI?"
    })

    assert result["answer"] is not None
    assert len(result["answer"]) > 0
    assert "confidence" in result
