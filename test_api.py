from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API Key:", api_key)

client = genai.Client(api_key=api_key)

for model in client.models.list():
    print(model.name)

try:
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents="Say Hello"
    )

    print(response.text)

except Exception as e:
    print(type(e))
    print(e)