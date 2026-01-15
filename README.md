# Agentic AI RAG Chatbot

## Overview
This project implements a Retrieval-Augmented Generation (RAG) chatbot
that answers questions strictly based on the *Agentic AI eBook*.
The system uses LangGraph for orchestration, Pinecone as the vector database,
and HuggingFace models for embeddings and generation.

The chatbot ensures:
- No hallucination
- Strict grounding to the provided PDF
- Source context transparency
- Confidence scoring for each response

---

## Architecture
1. PDF Ingestion (Agentic AI eBook)
2. Text Chunking
3. Embedding Generation (HuggingFace)
4. Vector Storage (Pinecone)
5. LangGraph-based RAG Pipeline:
   - Retrieve relevant chunks
   - Generate grounded answer
   - Calculate confidence score
6. FastAPI backend with HTML/CSS frontend UI

---

## Tech Stack
- Python
- LangGraph
- Pinecone
- HuggingFace Transformers
- FastAPI
- PyTest
- HTML / CSS

---

## Setup Instructions

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt


Running the Application
uvicorn api.main:app --reload


Open browser:

http://127.0.0.1:8000

Sample Questions

What is Agentic AI?

How does Agentic AI differ from traditional AI systems?

What are the key components of an Agentic AI system?

What value does Agentic AI create for businesses?

Who introduced early concepts related to Agentic AI?

Testing
python -m pytest


All major components (PDF loading, chunking, embedding, retrieval, generation, and graph flow)
are covered with test cases.

Notes

The chatbot answers only if the information exists in the PDF

If the answer is not found, it responds:

"The answer is not found in the provided document."

No OpenAI or low-code tools are used