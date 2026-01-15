## Agentic AI RAG Chatbot

## Overview
This project implements a **Retrieval-Augmented Generation (RAG)** chatbot that answers
user questions **strictly based on the Agentic AI eBook**.

The system uses **LangGraph** for orchestration, **Pinecone** as the vector database,
and **HuggingFace models** for embeddings and text generation.
It is designed to avoid hallucination by enforcing strict document grounding.

---

## Features
- PDF ingestion and chunking
- Vector embeddings using HuggingFace
- Pinecone-based semantic retrieval
- LangGraph-based RAG pipeline
- Strict grounding to source document
- Confidence score for every response
- FastAPI backend with HTML/CSS frontend
- End-to-end test coverage using PyTest
- No OpenAI or low-code tools used

---

## Architecture


<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/10f85252-d34b-4eb0-b597-6000f800a445" />




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

### 1️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Pinecone Setup

### 3️⃣ Create Pinecone Account

1. Go to [https://www.pinecone.io](https://www.pinecone.io)
2. Sign up for a free account
3. Create a new **index** with:

   * **Name:** agentic-ai-rag
   * **Dimension:** 384
   * **Metric:** cosine

---

### 4️⃣ Create `.env` File (IMPORTANT)

Create a file named `.env` in the project root.

```env
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_INDEX_NAME=agentic-ai-rag
```

---

### 5️⃣ Configure `config.py`

```python
import os

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = "agentic-ai-rag"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "google/flan-t5-base"
```

---

## Ingest the PDF

Run the ingestion script to load the PDF into Pinecone:

```bash
python ingest/embed_store.py
```

(This will load, chunk, embed, and store the document vectors.)

---

## Run the Application

```bash
uvicorn api.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---


## Testing

Run all tests:

```bash
python -m pytest
```

All major components (ingestion, chunking, retrieval, generation, and graph flow)
are covered with automated tests.

---

## Screenshots

<img width="904" height="930" alt="Screenshot 2026-01-15 214613" src="https://github.com/user-attachments/assets/9705abac-31d8-4307-b002-3c2e79cbac23" />

<img width="861" height="897" alt="Screenshot 2026-01-15 214826" src="https://github.com/user-attachments/assets/dff5dd73-5d47-4e9a-9d9d-46ee312a9905" />

