import pytest

from fastapi import status
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)



def test_static_file_easy():
    # The static file "test.txt" is madatory for this project.
    
    # Given
    filename = "test.txt"
    path = f"/static/files/{filename}"

    # When
    response = client.get(path)

    # Then
    assert response.status_code == status.HTTP_200_OK
    assert response.content != None
    assert "text/plain" in response.headers.get("content-type")


def test_static_file_medium():
    # TODO: Add a test case
    # Given
    # When
    # Then
    pass


def test_static_file_hard():
    # TODO: Add a test case
    # Given
    # When
    # Then
    pass