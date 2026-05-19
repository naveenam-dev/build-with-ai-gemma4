from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Initialize the Gemini client
# The client automatically picks up GEMINI_API_KEY from the environment
client = genai.Client()

app = FastAPI(title="Gemma 4 API Backend")

# Configure CORS so the React frontend can communicate with this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    role: str
    text: str

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[Message]] = []

class ChatResponse(BaseModel):
    reply: str

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Endpoint for communicating with the Gemma model via Google AI Studio.
    """
    try:
        # Build the contents array from the history
        contents = []
        for msg in request.history:
            # Map frontend 'ai' role to 'model' for the API
            api_role = "model" if msg.role == "ai" else "user"
            contents.append({
                "role": api_role,
                "parts": [{"text": msg.text}]
            })
            
        # Append the current user message
        contents.append({
            "role": "user",
            "parts": [{"text": request.message}]
        })

        # Call the Gemma model through the Gemini API
        # 'gemma-4-31b-it' is the available Gemma 4 model endpoint on AI Studio
        response = client.models.generate_content(
            model='gemma-4-31b-it',
            contents=contents,
        )
        response_text = response.text
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        response_text = "I'm sorry, I encountered an error while connecting to the model."
    
    return ChatResponse(reply=response_text)

@app.get("/")
def read_root():
    return {"message": "Gemma 4 Backend is running!"}
