from app import app, entries, mock_database

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
    assert response.headers["Location"] == "/"  # Update the expected value

    # Check if the entry was added to the database
    entry = entries[0]
    assert entry is not None
    assert entry.content == "Test Entry Content"


def test_add_entry_with_happiness(client):
    response = client.post(
        "/add_entry_with_happiness",
        data={"content": "Test Entry Content", "happiness": "😃"},
    )
    assert response.status_code == 302
    assert response.headers["Location"] == "/"
    assert mock_database[0].content == "Test Entry Content"
    assert mock_database[0].happiness == "😃"
