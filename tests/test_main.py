import pytest
from fastapi.testclient import TestClient
from component_library.main import app

client = TestClient(app)


def test_get_index():
    response = client.get("http://localhost:8000")
    assert response.status_code == 200
    assert "<h1>Component Library</h1>" in response.text

def test_get_component():
    response = client.get("http://localhost:8000/component/test")
    assert response.status_code == 200
    assert "<h1>Test Component</h1>" in response.text

def test_component_not_found():
    response = client.get("http://localhost:8000/component/nonexistent")
    assert response.status_code == 404