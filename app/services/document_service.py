from app.utils.file_handler import save_file
from app.services.pdf_service import extract_text
from app.services.chunk_service import chunk_text

async def handle_upload(file):
    file_path = await save_file(file)

    # Step 1: Extract text
    text = extract_text(file_path)

    # Step 2: Chunk text
    chunks = chunk_text(text)

    return {
        "message": "File processed successfully",
        "chunks_count": len(chunks),
        "sample_chunk": chunks[0] if chunks else ""
    }