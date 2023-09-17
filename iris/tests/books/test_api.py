
def test_can_open_swagger(client):
    response = client.get("/docs/")
    assert response.status_code == 200

def test_can_open_openapi_schema(client):
    response = client.get("/docs/?format=openapi")
    assert response.status_code == 200


