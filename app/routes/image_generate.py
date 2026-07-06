from fastapi import APIRouter, HTTPException
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

    try:

        if not data.prompt.strip():
            raise HTTPException(
                status_code=400,
                detail="Prompt cannot be empty"
            )

        prompt = urllib.parse.quote(data.prompt)

        image_url = (
            f"https://image.pollinations.ai/prompt/{prompt}"
            "?width=1024"
            "&height=1024"
            "&model=flux"
        )

        return {
            "success": True,
            "prompt": data.prompt,
            "image_url": image_url
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )