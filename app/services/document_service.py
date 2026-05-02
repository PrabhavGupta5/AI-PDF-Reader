from app.utils.file_handler import save_file

async def handle_upload(file):
    file_path = await save_file(file)

    return {
        "message": "File uploaded successfully",
        "file_path": file_path
    }