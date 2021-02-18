def test_liveness(client):
    """Liveness endpoint should always return 200 OK"""
    response = client.get('/health/alive')
    assert_200ok_and_json(response)


def test_readiness(client):
    """Readiness endpoint should always return 200 OK"""
    response = client.get('/health/ready')
    assert_200ok_and_json(response)


def assert_200ok_and_json(response):
    assert response.status_code == 200
    content_type_header = response.headers.get('Content-Type')
    assert content_type_header is not None
    assert content_type_header.lower() == 'application/json'
