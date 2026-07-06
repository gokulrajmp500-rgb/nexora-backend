import urllib.parse

def generate_image(prompt: str):

    encoded_prompt = urllib.parse.quote(prompt)

    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

    return image_url