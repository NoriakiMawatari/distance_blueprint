from decimal import Decimal

import pytest
from decouple import config
from yandex_geocoder import Client


def test_distance_to(client):
    # Test that viewing the page renders without template errors
    address = "Россия, Москва, Красная площадь"  # Red Square in russian
    response = client.get(f"/distance/{address}")
    assert response.status_code == 200
    assert b"Specified Address" in response.data
    assert b"Coordinates" in response.data
    assert b'<div id="map"></div>' in response.data

    yandex_client = Client(config("yandex_token"))
    coords = yandex_client.coordinates(address)
    confirm_address = yandex_client.address(coords[0], coords[1])
    assert confirm_address == address
    assert coords == (Decimal("37.621094"), Decimal("55.753605"))


def get_results(client, address, distance, time):
    return client.post(
        f"/distance/{address}/results",
        json=dict(address=address, distance=distance, time=time),
        follow_redirects=True,
    )


@pytest.mark.parametrize(
    ("address", "distance", "travel_time"),
    (
        ("Red Square", "11 mi", "27 min"),
        ("Mytischi", "4.3 mi", "11 min"),
        ("MKAD, 96th kilometre", None, None),
    ),
)
def test_results(client, address, distance, travel_time):
    response = get_results(
        client, address, distance=distance, time=travel_time
    )
    print(response)
    assert response.status_code == 200
