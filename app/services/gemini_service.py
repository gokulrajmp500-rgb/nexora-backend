import os
import io

from PIL import Image
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")


# ==========================
# CHAT
# ==========================
def ask_gemini(prompt: str):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return str(e)


# ==========================
# IMAGE ANALYZE
# ==========================
def analyze_image(image_bytes: bytes, prompt: str):
    try:
        # Convert bytes into PIL Image
        image = Image.open(io.BytesIO(image_bytes))

        response = model.generate_content([
            prompt,
            image
        ])

        return response.text

    except Exception as e:
        return str(e)