from fastapi import FastAPI
from app.api.routes import router as items

app = FastAPI(title = "AI PDF Reader")

app.include_router(items)