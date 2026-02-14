import json
from app.api import app

def test_health_endpoint():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert data["status"] == "ok"

def test_simulate_endpoint():
    client = app.test_client()
    resp = client.post("/simulate", json={"h_coeff": 0.5, "t_final": 5, "steps": 50})
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert "t" in data and "expect_x" in data

def test_surrogate_endpoint():
    client = app.test_client()
    resp = client.post("/surrogate_predict", json={"features": {"atomic_number_sum": 3}})
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert "predicted_energy" in data
