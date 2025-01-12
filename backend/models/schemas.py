from pydantic import BaseModel


# Define Pydantic schemas for validation
class Message(BaseModel):
    """
    Represents a validation model for a message using Pydantic.

    Attributes:
    ----------
    message : str
        The content of the message to be validated.
    """
    message: str