import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


# ✅ CHAT FUNCTION
def ask_gemini(prompt: str):
    response = model.generate_content(prompt)
    return response.text


# ✅ IMAGE ANALYZE FUNCTION (IMPORTANT - THIS WAS MISSING)
def analyze_image(image_bytes: bytes, prompt: str):
    response = model.generate_content([
        prompt,
        image_bytes
    ])
    return response.text