def test_metrics_endpoint(client):
    response = client.get("/metrics")
    assert response.status_code == 200
