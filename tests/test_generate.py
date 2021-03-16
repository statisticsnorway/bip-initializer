import json
from .inputs import required_input
from .outputs import required_output


def test_generate_exposed_with_authentication(client):
    response = client.post(
        "/api/v1/generate",
        headers={"Content-Type": "application/json"},
        json=json.loads(required_input()),
    )
    assert response.status_code == 200
    assert response.json() == json.loads(required_output())


def test_generate_unexposed_with_authentication(client):
    post_data = json.loads(required_input())
    post_data["exposed"] = False
    response = client.post(
        "/api/v1/generate",
        headers={"Content-Type": "application/json"},
        json=post_data,
    )
    assert response.status_code == 200
    assert response.json()["spec"]["values"]["exposed"] == "False"


def test_wrong_type(client):
    post_data = json.loads(required_input())
    post_data["port"] = "Femhundre"
    response = client.post(
        "/api/v1/generate",
        headers={"Content-Type": "application/json"},
        json=post_data,
    )
    assert response.status_code == 422


def test_missing_value(client):
    post_data = json.loads(required_input())
    del post_data["cluster"]
    print(post_data)
    response = client.post(
        "/api/v1/generate",
        headers={"Content-Type": "application/json"},
        json=post_data,
    )
    assert response.status_code == 422
