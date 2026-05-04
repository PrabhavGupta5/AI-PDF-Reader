from app.utils.file_handler import save_file
from app.services.pdf_service import extract_text
from app.services.chunk_service import chunk_text
from app.services.embedding_service import get_embedding
from app.services.vector_db_service import store_embeddings

def clean_text(text: str):
    text = text.replace("\n", " ")
    text = " ".join(text.split())
    return text

async def handle_upload(file):
    file_path = await save_file(file)

    text = clean_text(extract_text(file_path))
    chunks = chunk_text(text)

    embeddings = [get_embedding(chunk) for chunk in chunks]
    
    store_embeddings(chunks, embeddings)

    return {
        "message": "File processed + embeddings stored",
        "chunks": len(chunks)
    }