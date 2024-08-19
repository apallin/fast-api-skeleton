from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main() -> None:
    response = client.get("/hello-world")
    assert response.status_code == 200
    assert response.json() == "Hello World"
