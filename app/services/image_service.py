from urllib.parse import quote

def generate_image(prompt: str):
    prompt = quote(prompt)
    image_url = f"https://image.pollinations.ai/prompt/{prompt}"
    return image_url