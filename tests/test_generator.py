from rag.generator import get_llm

def test_generator():
    llm = get_llm()

    prompt = """
    Context:
    Agentic AI refers to AI systems capable of autonomous decision-making.

    Question:
    What is Agentic AI?
    """

    response = llm.invoke(prompt)

    assert response is not None
    assert len(response) > 0
