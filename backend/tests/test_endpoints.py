import pytest
from fastapi.testclient import  TestClient
from backend.main import app

client = TestClient(app)

def test_fetch_messages():
    response = client.get("/chat/history")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_send_message():
    response = client.post("/chat/message", json={"message": "Hello Chatbot"})
    assert response.status_code == 200
    json_response = response.json()
    assert json_response.get("status") == "Success"