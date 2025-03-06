import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key dari file .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

try:
    models = genai.list_models()
    print("Daftar model yang tersedia:")
    for model in models:
        print("-", model.name)
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
