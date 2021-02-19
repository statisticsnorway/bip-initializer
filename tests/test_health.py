def test_liveness(client):
    response = client.get("/health/alive")
    assert response.status_code == 200


def test_readiness(client):
    response = client.get("/health/ready")
    assert response.status_code == 200
