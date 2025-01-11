import pytest
from fastapi.testclient import  TestClient
from backend.main import app

client = TestClient(app)

def test_chat_flow():
    # Send a message
    response = client.post("/chat/message", json={"message": "Integration Test Message"})
    assert response.status_code == 200

    # Fetch messages
    response = client.get("/chat/history")
    assert response.status_code == 200
    messages = response.json()
    assert any(msg["message"] == "Integration Test Message" for msg in messages)
    assert len(messages) == 2  # User message + AI response
    assert messages[0]["user"] == "User"
    assert messages[1]["user"] == "AI"