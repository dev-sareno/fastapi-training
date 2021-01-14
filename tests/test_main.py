from fastapi import status
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)



def test_main_easy():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK


def test_main_medium():
    assert True


def test_main_hard():
    assert True