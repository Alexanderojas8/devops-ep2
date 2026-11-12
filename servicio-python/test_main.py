from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_saludo():
    r = client.get("/saludo")
    assert r.status_code == 200
    assert r.json() == {"mensaje": "Hola desde Python"}


def test_restar():
    r = client.get("/restar", params={"a": 5, "b": 3})
    assert r.json() == {"resultado": 2}