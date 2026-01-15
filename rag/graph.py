from typing import TypedDict, List
from langgraph.graph import StateGraph

from rag.retriever import get_retriever
from rag.generator import get_llm


# ---------
# State
# ---------
class RAGState(TypedDict):
    question: str
    docs: List[str]
    answer: str
    confidence: float


retriever = get_retriever()
llm = get_llm()


# ---------
# Nodes
# ---------
def retrieve_node(state: RAGState):
    docs = retriever.invoke(state["question"])
    return {"docs": docs}


def generate_node(state: RAGState):
    context = "\n\n".join([d.page_content for d in state["docs"]])

    prompt = f"""
You are an expert RAG-based chatbot.

You must answer the user's question using ONLY the content from the Agentic AI eBook.

Rules:
- Use only the provided context.
- Do NOT use prior knowledge.
- Do NOT infer or guess.
- If the answer is not explicitly stated in the context, reply exactly with:
  "The answer is not found in the provided document."

Context:
{context}

Question:
{state["question"]}
"""

    raw_answer = llm.invoke(prompt)

    # Hallucination guard
    if "not found in the provided document" in raw_answer.lower():
        return {
            "answer": "The answer is not found in the provided document."
        }

    return {
        "answer": raw_answer
    }



def confidence_node(state: RAGState):
    confidence = min(len(state["docs"]) / 4, 1.0)
    return {"confidence": confidence}


# ---------
# Build Graph
# ---------
def build_graph():
    graph = StateGraph(RAGState)

    graph.add_node("retrieve", retrieve_node)
    graph.add_node("generate", generate_node)
    graph.add_node("confidence", confidence_node)

    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "generate")
    graph.add_edge("generate", "confidence")

    return graph.compile()
