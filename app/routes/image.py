from fastapi import APIRouter, UploadFile, File, Form
from app.services.gemini_service import analyze_image

router = APIRouter(prefix="/image", tags=["Image"])


@router.post("/analyze")
async def image_analyze(
    image: UploadFile = File(...),
    prompt: str = Form("Describe this image")
):
    image_bytes = await image.read()

    result = analyze_image(image_bytes, prompt)

    return {
        "result": result
    }