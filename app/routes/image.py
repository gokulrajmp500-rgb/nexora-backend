from fastapi import APIRouter
from app.services.image_generate_service import generate_image

router = APIRouter()

# IMAGE GENERATE ROUTE
@router.post("/generate")
async def create_image(data: dict):
    prompt = data["prompt"]
    image = generate_image(prompt)

    return {
        "message": "success",
        "image": image
    }