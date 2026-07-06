import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print(os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini(prompt: str):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return str(e)


def analyze_image(image_bytes: bytes, prompt: str):
    try:
        response = model.generate_content([
            prompt,
            image_bytes,
        ])
        return response.text
    except Exception as e:
        return str(e)