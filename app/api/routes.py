from fastapi import APIRouter, UploadFile, File
from app.services.document_service import handle_upload
from app.services.embedding_service import get_embedding
from app.services.vector_db_service import search_similar
from app.services.llm_service import generate_answer

router = APIRouter()

@router.get("/")
def health():
    return {"status": "running"}

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return await handle_upload(file)

@router.get("/query")
def query(q: str):
    # Step 1: Convert query → embedding
    query_embedding = get_embedding(q)
    # Step 2: Retrieve relevant chunks
    docs = search_similar(query_embedding)
    # Step 3: Generate final answer
    answer = generate_answer(q, docs)

    return {
        "query": q,
        "answer": answer,
        "sources": docs
    }