from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.chat import router as chat_router
from app.routes.image import router as image_router

app = FastAPI(title="NEXORA AI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(image_router)


@app.get("/")
def home():
    return {
        "status": "running",
        "message": "NEXORA AI Backend"
    }