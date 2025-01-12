from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models.schemas import Message
from models.database import SessionLocal
from loggers import get_chat_logger
from models.models import  ChatMessage
from gen_ai_response import get_ai_response


router = APIRouter()
logger = get_chat_logger(__name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def root():
    """
    Root endpoint that acts as a health check or welcome message.

    Returns:
        dict: A simple welcome message as JSON response.

    Raises:
        HTTPException: If any error occurs during processing.
    """
    try:
        logger.info("Root endpoint accessed")  # Log the access to the root endpoint

        return {"message": "Hello to AI Assistant"}  # Return a simple greeting message
    except Exception as e:
        logger.error(f"Error in root endpoint: {e}")  # Log any exception that occurs
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/chat/message")
async def post_message(msg: Message, db: Session = Depends(get_db)):
    """
    Endpoint to handle posting a new chat message and generating AI response.

    Args:
        msg (Message): The message object containing the user's input message.
        db(Session)

    Returns:
        dict: A dictionary containing the success status and AI's response.

    Raises:
        HTTPException: If an error occurs while processing the message or generating response.
    """
    try:
        logger.info(f"Received message: {msg.message}")  # Log the received user message

        user_message = ChatMessage(user="User", message=msg.message)  # Create a chat message object for the user

        db.add(user_message)  # Add user message to the database session
        db.commit()  # Commit the transaction to save the message
        db.refresh(user_message)

        response = get_ai_response(user_message.message)  # Generate AI response based on user message
        if not response:
            logger.error("AI response is empty or None")
            raise HTTPException(status_code=500, detail="AI response is empty or None")

        if not response:  # Check if the AI response is invalid or empty

            logger.error("AI response is empty or None")  # Log if AI response is invalid

            raise HTTPException(status_code=500, detail="AI response is empty or None")  # Raise error for empty AI response

        ai_message = ChatMessage(user="AI", message=response)
        # Create a chat message object for the AI
        db.add(ai_message)  # Add AI message to the database session
        db.commit()  # Commit the transaction to save the AI message
        db.refresh(ai_message)

        logger.info(f"AI response: {response}")  # Log the generated AI response
        return {"status": "Success", "response": response}
    except Exception as e:
        logger.error(f"Error processing message: {e}")  # Log any exception that occurs during message processing
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/chat/history")
async def get_history(db: Session = Depends(get_db)):
    """
    Endpoint to retrieve the chat history.

    Returns:
        list: List of ChatMessage objects representing the chat history.

    Raises:
        HTTPException: If an error occurs while retrieving the history.
    """
    try:
        logger.info("Chat history requested")  # Log when chat history is requested

        history = db.query(ChatMessage).all()  # Retrieve all chat messages from the database
        return history  # Return the chat history as a response
    except Exception as e:
        logger.error(f"Error retrieving chat history: {e}")  # Log any errors that occur during chat history retrieval
        raise HTTPException(status_code=500, detail="Internal Server Error")
