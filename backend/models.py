from pydantic import BaseModel
from typing import List

# Define a Pydantic model to represent a basic message structure
class Message(BaseModel):
    message: str

# Define another Pydantic model to represent user-specific chat messages
class ChatMessage(BaseModel):
    user:str
    message: str

# A list to keep the chat history; each entry is a ChatMessage object
chat_history: List[ChatMessage] = [] # Simple in-memory DB