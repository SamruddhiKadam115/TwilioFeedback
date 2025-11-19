from fastapi import APIRouter, Form, Depends
from fastapi.responses import Response
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend import models
from typing import Dict

router = APIRouter()

# In-memory session store (in production, use Redis or similar)
user_sessions: Dict[str, dict] = {}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/whatsapp")
async def whatsapp_webhook(
    From: str = Form(...),
    Body: str = Form(...),
    db: Session = Depends(get_db)
):
    """
    Handle incoming WhatsApp messages from Twilio.
    Twilio sends: From (phone number) and Body (message text)
    """
    phone = From
    message = Body.strip()
    
    print(f"Received message from {phone}: {message}")  # Debug logging
    
    # Initialize session if new user
    if phone not in user_sessions:
        user_sessions[phone] = {
            "step": "init",
            "product_name": None,
            "user_name": None,
            "product_review": None
        }
    
    session = user_sessions[phone]
    response_message = ""
    
    # Conversation flow
    if session["step"] == "init":
        # First message from user
        session["step"] = "ask_product"
        response_message = "Which product is this review for?"
    
    elif session["step"] == "ask_product":
        session["product_name"] = message
        session["step"] = "ask_name"
        response_message = "What's your name?"
    
    elif session["step"] == "ask_name":
        session["user_name"] = message
        session["step"] = "ask_review"
        response_message = f"Please send your review for {session['product_name']}."
    
    elif session["step"] == "ask_review":
        session["product_review"] = message
        
        # Save to database
        new_review = models.Review(
            contact_number=phone,
            user_name=session["user_name"],
            product_name=session["product_name"],
            product_review=session["product_review"]
        )
        db.add(new_review)
        db.commit()
        
        response_message = f"Thanks {session['user_name']} -- your review for {session['product_name']} has been recorded."
        
        # Reset session
        user_sessions[phone] = {
            "step": "init",
            "product_name": None,
            "user_name": None,
            "product_review": None
        }
    
    print(f"Sending response: {response_message}")  # Debug logging
    
    # Return TwiML response with proper content type
    twiml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>{response_message}</Message>
</Response>"""
    
    return Response(content=twiml, media_type="application/xml")