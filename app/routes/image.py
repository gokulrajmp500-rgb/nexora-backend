from fastapi import APIRouter, UploadFile, File, Form
from app.services.image_service import analyze_image

router = APIRouter(
    prefix="/image",
    tags=["Image Analyze"]
)

@router.post("/analyze")
async def image_analyze(
    image: UploadFile = File(...),
    prompt: str = Form(...)
):
    result = await analyze_image(image, prompt)
    return result