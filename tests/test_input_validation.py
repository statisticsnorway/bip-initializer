import json
from .inputs import required_input
from .outputs import required_output


def test_validate_input_too_long(client):
    post_data = json.loads(required_input())
    post_data[
        "name"
    ] = "Detteerenkjempelangstrensomskalfeilemeserabeltogsomikkegitnoenmeningidetheletatt"
    response = client.post(
        "/api/v1/generate",
        headers={"Content-Type": "application/json"},
        json=post_data,
    )
    print(json.dumps(response.json()))
    assert response.status_code == 422


def test_validate_input_too_short(client):
    post_data = json.loads(required_input())
    post_data["name"] = ""
    response = client.post(
        "/api/v1/generate",
        headers={"Content-Type": "application/json"},
        json=post_data,
    )
    print(json.dumps(response.json()))
    assert response.status_code == 422


def test_validate_input_invalid_characters(client):
    post_data = json.loads(required_input())
    post_data["name"] = "Skal-ikke-virke-med-bindestrek-bakerst-"
    response = client.post(
        "/api/v1/generate",
        headers={"Content-Type": "application/json"},
        json=post_data,
    )
    print(json.dumps(response.json()))
    assert response.status_code == 422


def test_validate_input_invalid_characters(client):
    post_data = json.loads(required_input())
    post_data["name"] = "Skal-ikke-virke-med-bindestrek-bakerst-"
    response = client.post(
        "/api/v1/generate",
        headers={"Content-Type": "application/json"},
        json=post_data,
    )
    print(json.dumps(response.json()))
    assert response.status_code == 422


def test_validate_input_valid_characters(client):
    post_data = json.loads(required_input())
    post_data[
        "image_repository"
    ] = "eu.gcr.io/prod-bip/ssb/tidsbruk/timeuse-survey-service"
    response = client.post(
        "/api/v1/generate",
        headers={"Content-Type": "application/json"},
        json=post_data,
    )
    print(json.dumps(response.json()))
    assert response.status_code == 200


def test_flux_image_tag_does_not_start_correctly(client):
    post_data = json.loads(required_input())
    post_data["flux_image_tag_pattern"] = "funkeritte-*"
    response = client.post(
        "/api/v1/generate",
        headers={"Content-Type": "application/json"},
        json=post_data,
    )
    print(json.dumps(response.json()))
    assert response.status_code == 422


def test_flux_image_tag_starts_correctly(client):
    post_data = json.loads(required_input())
    post_data["flux_image_tag_pattern"] = "glob:main-*"
    response = client.post(
        "/api/v1/generate",
        headers={"Content-Type": "application/json"},
        json=post_data,
    )
    print(json.dumps(response.json()))
    assert response.status_code == 200


def test_unwanted_priviliged_port(client):
    post_data = json.loads(required_input())
    post_data["port"] = 80
    response = client.post(
        "/api/v1/generate",
        headers={"Content-Type": "application/json"},
        json=post_data,
    )
    print(json.dumps(response.json()))
    assert response.status_code == 422


def test_boolean(client):
    post_data = json.loads(required_input())
    post_data["exposed"] = "fal"
    response = client.post(
        "/api/v1/generate",
        headers={"Content-Type": "application/json"},
        json=post_data,
    )
    print(json.dumps(response.json()))
    assert response.status_code == 422
