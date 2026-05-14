AI PDF Chatbot (RAG)

An AI-powered conversational document assistant that allows users to upload PDF documents and ask natural language questions over their content using Retrieval-Augmented Generation (RAG).

⸻

Overview

This project enables context-aware question answering on uploaded documents by combining:

* Semantic Search
* Vector Embeddings
* Retrieval-Augmented Generation (RAG)
* Google Gemini API
* ChromaDB Vector Database

The system processes uploaded PDFs, converts them into vector embeddings, retrieves relevant chunks during queries, and generates grounded responses using an LLM.

⸻

Features

* Upload PDF documents
* Extract and clean document text
* Chunk large documents intelligently
* Generate embeddings using Gemini Embedding Models
* Store embeddings in ChromaDB
* Perform semantic similarity search
* Generate contextual answers using Gemini LLM
* REST APIs with FastAPI
* Interactive Swagger UI documentation

⸻

Architecture

        User Uploads PDF
                ↓
        Text Extraction
                ↓
        Text Cleaning
                ↓
        Chunking
                ↓
        Embedding Generation
                ↓
        ChromaDB Vector Storage
                ↓
        User Query
                ↓
        Similarity Search
                ↓
        Relevant Chunks Retrieved
                ↓
        Gemini LLM
                ↓
        Context-Aware Answer

⸻

Tech Stack

Backend

* Python
* FastAPI

AI / RAG

* Google Gemini API
* Embeddings
* Retrieval-Augmented Generation (RAG)

Vector Database

* ChromaDB

Utilities

* PyPDF2
* LangChain Text Splitters
* Uvicorn

⸻

Project Structure

        ai-pdf-chatbot/
        │
        ├── app/
        │   ├── main.py
        │   ├── api/
        │   │   └── routes.py
        │   ├── services/
        │   │   ├── document_service.py
        │   │   ├── embedding_service.py
        │   │   ├── vector_service.py
        │   │   └── llm_service.py
        │   ├── utils/
        │   │   └── file_handler.py
        │   └── schemas/
        │       └── request_schema.py
        │
        ├── uploads/
        ├── requirements.txt
        ├── .env
        └── README.md

⸻

API Endpoints

Upload PDF

POST /upload

Uploads a PDF document, extracts text, chunks content, generates embeddings, and stores vectors in ChromaDB.

⸻

Query Document

POST /query

Example Request:

{
  "query": "Summarize this document"
}

Example Response:

{
  "answer": "Generated contextual answer",
  "sources": ["Relevant chunk 1", "Relevant chunk 2"]
}

⸻

Setup Instructions

Clone Repository

git clone <your-github-repo>
cd ai-pdf-chatbot

⸻

Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

⸻

Install Dependencies

pip install -r requirements.txt

⸻

Configure Environment Variables

Create a .env file:

GEMINI_API_KEY=your_api_key_here

⸻

Run Application

python3 -m uvicorn app.main:app --reload

Swagger UI:

http://127.0.0.1:8000/docs

⸻

What Problems This Project Solves

* Enables efficient document understanding
* Eliminates manual searching across PDFs
* Improves contextual question answering
* Reduces hallucination using retrieved context
* Demonstrates production-ready AI backend architecture

⸻

Key Learnings

* Retrieval-Augmented Generation (RAG)
* Vector embeddings and semantic search
* Chunking strategies for LLMs
* FastAPI backend development
* Vector databases and retrieval pipelines
* Prompt grounding techniques
* AI system architecture design

⸻

Future Improvements

* Multi-document support
* User authentication
* Redis caching
* Async ingestion pipeline
* AWS deployment
* Docker containerization
* Streaming responses
* Hybrid keyword + semantic search
* Chat history memory
* Role-based access control

⸻

Resume Highlights

* Built an end-to-end RAG pipeline
* Integrated Gemini API with vector retrieval
* Implemented semantic similarity search
* Developed scalable ingestion architecture
* Built production-style AI backend services

⸻

Author

Prabhav Gupta
