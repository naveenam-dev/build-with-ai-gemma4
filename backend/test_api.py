import os
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

load_dotenv()
client = genai.Client()

try:
    print("Testing gemini-1.5-flash...")
    response = client.models.generate_content(
        model='gemini-1.5-flash',
        contents='Hello'
    )
    print("gemini-1.5-flash success!")
except Exception as e:
    print(f"gemini-1.5-flash error: {e}")

try:
    print("Testing gemma-2-9b-it...")
    response = client.models.generate_content(
        model='gemma-2-9b-it',
        contents='Hello'
    )
    print("gemma-2-9b-it success!")
except Exception as e:
    print(f"gemma-2-9b-it error: {e}")

try:
    print("Testing gemma-2-2b-it...")
    response = client.models.generate_content(
        model='gemma-2-2b-it',
        contents='Hello'
    )
    print("gemma-2-2b-it success!")
except Exception as e:
    print(f"gemma-2-2b-it error: {e}")
