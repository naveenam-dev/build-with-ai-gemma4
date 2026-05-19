import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

history = [
    {"role": "user", "parts": [{"text": "My favorite color is blue."}]},
    {"role": "model", "parts": [{"text": "Got it, your favorite color is blue."}]}
]

contents = history + [{"role": "user", "parts": [{"text": "What is my favorite color?"}]}]

try:
    response = client.models.generate_content(
        model='gemma-4-31b-it',
        contents=contents
    )
    print("Success! Response:")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
