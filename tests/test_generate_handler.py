def test_generate_handler(client):
    response = client.post(
        "/api/1/generate",
        headers={"Content-Type": "application/json"},
        json={
            "name": "string",
            "namespace": "string",
            "cluster": "string",
            "billingproject": "string",
            "image_repository": "string",
            "image_tag": "string",
            "port": 80,
            "serviceaccount_create": True,
            "apptype": "backend",
            "exposed": False,
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "string",
        "namespace": "string",
        "cluster": "string",
        "billingproject": "string",
        "image_repository": "string",
        "image_tag": "string",
        "port": 80,
        "serviceaccount_create": True,
        "apptype": "backend",
        "exposed": False,
    }
