from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

app = FastAPI(
    title="AI Receptionist API"
)

class ReceptionistRequest(BaseModel):
    message: str


@app.post("/api/receptionist/respond")
def receptionist_response(req: ReceptionistRequest):

    if not req.message.strip():
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty"
        )

    prompt = f"""
You are an AI receptionist for a salon.

Business Hours:
9:00 AM - 6:00 PM

Available Appointment Slots:
- 10:00 AM
- 2:00 PM
- 4:30 PM

Possible intents:
- appointment_booking
- business_hours
- pricing_query
- general_question

Customer Message:
{req.message}

Format:
{{
    "intent": "...",
    "response": "..."
}}
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    result = completion.choices[0].message.content

    return json.loads(result)
