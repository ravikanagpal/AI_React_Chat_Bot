import random

from loggers import get_chat_logger

logger = get_chat_logger(__name__)

DUMMY_RESPONSES = [
    "Hi there! I'm a simulated AI assistant.",
    "Hello! This is a placeholder AI response.",
    "I'm just a dummy function pretending to be AI.",
    "That's an interesting point! Let me think about it...",
    "I understand what you're saying. Please tell me more!"
]

def get_ai_response(user_message: str) -> str:
    """
    Returns a randomly selected dummy response.
    In a real application, you'd replace this with an actual AI/LLM call.
    """
    logger.info(f"Generating AI response for message: {user_message}")
    # Uncomment and use the following code to integrate OpenAI's API
    # from dotenv import load_dotenv
    # import os
    #
    # load_dotenv()
    # api_key = os.getenv("LLM_API_KEY")
    # import openai
    # try:
    #   openai.api_key = api_key  # Replace with your OpenAI API key
    #   response = openai.Completion.create(
    #     engine="gpt-4",  # Specify the model to use
    #     prompt=user_message,
    #     max_tokens=150
    #   )
    #   return response.choices[0].text.strip()
    # except Exception as e:
    #   logger.error(f"Error generating AI response: {e}")
    #   return "Sorry, I am unable to process your request at the moment"
    return random.choice(DUMMY_RESPONSES)