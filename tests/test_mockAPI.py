import pytest
from AUTOMATION.MockAPI import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_mock_endpoint_without_setup(client):
    """
    Test API before setting mock_method (should fail or return 405)
    """
    response = client.get("/mock")
    assert response.status_code in [405, 500]


def test_mock_get_request_success(client, monkeypatch):
    """
    Simulate GET method setup and validate response
    """

    # Mock global variables inside your app
    import MockAPI
    MockAPI.mock_method = "GET"
    MockAPI.mock_response = {"status": "success"}

    response = client.get("/mock")

    assert response.status_code == 200
    assert response.json == {"status": "success"}


def test_mock_post_wrong_method(client, monkeypatch):
    """
    Validate incorrect method handling
    """

    import MockAPI
    MockAPI.mock_method = "GET"
    MockAPI.mock_response = {"status": "success"}

    response = client.post("/mock")

    assert response.status_code == 405
    assert "Only GET method is allowed" in response.json["error"]