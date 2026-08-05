from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")

print("GEMINI API Key:", GEMINI_API_KEY)
print("WEATHER API Key:", WEATHER_API_KEY)
print("MONGO_URI:", MONGO_URI)