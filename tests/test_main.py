import pytest

from fastapi import status
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)



def test_main_easy():
    # Given
    path = "/"

    # When
    response = client.get(path)

    # Then
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"Hello": "World"}


def test_main_medium():
    # Given
    path = "/"

    # When
    response = client.get(path)

    # Then
    #   Ensure the response has only 1 key in lenglth
    assert len(response.json().keys()) == 1
    #   Ensure the "Hello" in response existed
    assert response.json().get("Hello") != None


def test_main_hard():
    # Given
    path = "/"

    # When
    response = client.post(path)

    # Then
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    assert response.json() == {"detail": "Method Not Allowed"}