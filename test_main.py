from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_time_not_zero():
    response = client.get("/time")
    assert response.status_code == 200
    data = response.json()
    assert data["time"] != 0

def test_metrics_count():
    client.get("/time")
    response = client.get("/metrics")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] > 0
