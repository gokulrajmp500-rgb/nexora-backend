from fastapi import FastAPI

from app.routes.chat import router as chat_router
from app.routes.image import router as image_router
from app.routes.image_generate import router as image_generate_router


app = FastAPI(
    title="NEXORA AI Backend",
    version="1.0.0"
)
@app.get("/")
def home():
    return {
        "status": "running",
        "message": "NEXORA AI Backend"
    }

# Chat AI
app.include_router(chat_router)

# Image Analysis
app.include_router(image_router)

# Image Generation
app.include_router(image_generate_router)