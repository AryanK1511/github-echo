import google.generativeai as genai

from _config import GOOGLE_GEMINI_API_KEY

genai.configure(api_key=GOOGLE_GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)
