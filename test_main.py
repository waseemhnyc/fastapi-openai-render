from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_prompt():
    response = client.post("/prompt/", json={"message": "Hello AI!"})
    assert response.status_code == 200
    assert "response" in response.json()


def test_prompt_stream():
    response = client.post("/prompt/stream/", json={"message": "Hello AI!"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/event-stream; charset=utf-8"
