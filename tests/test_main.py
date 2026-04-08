import json
from app.main import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_add_valid():
    client = app.test_client()
    response = client.post("/add", json={"a": 2, "b": 3})
    data = json.loads(response.data)
    assert data["result"] == 5
