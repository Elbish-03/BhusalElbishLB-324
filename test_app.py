from app import app

import pytest


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    client = app.test_client()

    yield client


def test_add_entry(client):
    # Test adding an entry
    response = client.post("/add_entry", data={"content": "Test Entry Content"})

    assert response.status_code == 302
    assert (
        response.headers["Location"] == "http://localhost/"
    )  # Update the expected value
