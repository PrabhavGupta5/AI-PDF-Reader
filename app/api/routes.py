from fastapi import APIRouter, UploadFile, File
from app.services.document_service import handle_upload
from app.services.embedding_service import get_embedding
from app.services.vector_db_service import search_similar

router = APIRouter()

@router.get("/")
def health():
    return {"status": "running"}

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return await handle_upload(file)

@router.get("/query")
def query(q: str):
    query_embedding = get_embedding(q)
    docs = search_similar(query_embedding)

    return {
        "query": q,
        "results": docs
    }