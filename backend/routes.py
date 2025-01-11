from fastapi import APIRouter, HTTPException

from loggers import get_chat_logger
from models import Message, ChatMessage, chat_history
from gen_ai_response import get_ai_response


router = APIRouter()
logger = get_chat_logger(__name__)

@router.get("/")
async def root():
    try:
        logger.info("Root endpoint accessed")
        return {"message": "Hello to AI Assistant"}
    except Exception as e:
        logger.error(f"Error in root endpoint: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/chat/message")
async def post_message(msg: Message):
    try:
        logger.info(f"Received messageL: {msg.message}")
        user_message = ChatMessage(user="User", message=msg.message)
        chat_history.append(user_message)
        response = get_ai_response(user_message.message)
        if not response:
            logger.error("AI response is empty or None")
            raise HTTPException(status_code=500, detail="AI response is empty or None")

        ai_message = ChatMessage(user="AI", message=response)
        chat_history.append(ai_message)
        logger.info(f"AI response: {response}")
        return {"status": "Success", "response": response}
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/chat/history")
async def get_history():
    try:
        logger.info("Chat history requested")
        return chat_history
    except Exception as e:
        logger.error(f"Error retrieving chat history: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
