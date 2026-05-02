from fastapi import APIRouter, UploadFile, File
from app.services.document_service import handle_upload

router = APIRouter()

@router.get("/")
def health():
    return {"status": "running"}

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return await handle_upload(file)

@router.get("/query")
def query(q: str):
    return {"message": f"Query received: {q}"}