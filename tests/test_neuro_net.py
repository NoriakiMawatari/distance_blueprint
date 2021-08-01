from neuro_net import __version__


def test_version():
    assert __version__ == "0.1.0"


def submit_address(client, address):
    return client.post("/", data=dict(address=address), follow_redirects=True)


def test_index_route(client):
    # Testing GET method
    response = client.get("/")
    assert response.status_code == 200
    assert b'<label for="address">Addres:</label>' in response.data
    assert b'<div id="map"></div>' not in response.data

    # Testing POST method
    address = "Red Square"
    response = submit_address(client, address)
    assert b"Specified Address" in response.data

    # Testing invalid address input
    response = submit_address(client, " ")
    assert b"Addres:" in response.data
