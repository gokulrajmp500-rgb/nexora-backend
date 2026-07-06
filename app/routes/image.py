from fastapi import APIRouter, UploadFile, File, Form
from app.services.gemini_service import analyze_image

router = APIRouter(
    prefix="/image",
    tags=["Image Analyze"]
)

@router.post("/analyze")
async def image_analyze(
    image: UploadFile = File(...),
    prompt: str = Form(...)
):
    image_bytes = await image.read()

    result = analyze_image(image_bytes, prompt)

    return {
        "success": True,
        "result": result
    }