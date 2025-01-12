from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime, timezone


# Define the DeclarativeBase for SQLAlchemy
class Base(DeclarativeBase):
    """
    Base class for SQLAlchemy ORM models.

    This class serves as the foundation for all ORM models in the application.
    It inherits from SQLAlchemy's DeclarativeBase to enable declarative model
    definitions.
    """
    pass


class ChatMessage(Base):
    """
    Represents a chat message record in the 'chat_messages' table.

    Attributes:
        id (Integer): The primary key for the chat message record.
        user (String): The username of the user who sent the message.
        message (Text): The content of the chat message.
        timestamp (DateTime): The timestamp when the message was sent.
                              Defaults to the current UTC time.
    """
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True)
    user = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))