import pytest
from fastapi.testclient import TestClient
from component_library.main import app
from pathlib import Path

client = TestClient(app)

def test_get_button_component():
    response = client.get("/component/button")
    assert response.status_code == 200
    assert 'class="inline-flex items-center justify-center' in response.text

def test_button_click():
    response = client.post("/button-click")
    assert response.status_code == 200
    assert '<div id="showcase"' in response.text

def test_component_not_found():
    response = client.get("/component/nonexistent")
    assert response.status_code == 404