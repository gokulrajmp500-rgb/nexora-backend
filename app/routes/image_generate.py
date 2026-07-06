from fastapi import APIRouter
from pydantic import BaseModel
import urllib.parse

router = APIRouter(
    prefix="/image",
    tags=["Image Generate"]
)

class PromptRequest(BaseModel):
    prompt: str

@router.post("/generate")
async def create_image(data: PromptRequest):

    encoded_prompt = urllib.parse.quote(data.prompt)

    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

    return {
        "success": True,
        "image_url": image_url
    }