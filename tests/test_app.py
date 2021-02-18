def test_hello(client):
    """Hello endpoint should return 200 OK and a body containing a string starting with Hello"""
    response = client.get('/hello')
    assert response.status_code == 200
    assert b'Hello' in response.data
