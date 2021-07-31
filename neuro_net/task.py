import logging as log

from decouple import config
from flask import Blueprint, render_template
from yandex_geocoder import Client, NothingFound

distance = Blueprint("distance", __name__, url_prefix="/distance")


@distance.route("/<address>", methods=["GET", "POST"])
def distance_to(address: str) -> str:
    error = None
    if not address:
        error = "Address needed."
        log.error(error)
    log.info(f"The address is: {address}")
    if error is None:
        try:
            # Yandex Maps API token required to instance the client. In order
            # to acquire it register on
            # https://developer.tech.yandex.ru/services/
            client = Client(config("yandex_token"))
            coordinates = client.coordinates(address)
            log.info(
                f"Coords of address: [{coordinates[1]}, {coordinates[0]}]"
            )

            direction = client.address(coordinates[0], coordinates[1])
            log.info(f"Confirm the address from coords: {direction}")
            return render_template(
                "maps.html",
                api_key=config("yandex_token"),
                address_txt=address,
                address_lat=coordinates[1],
                address_lng=coordinates[0],
            )
        except NothingFound:
            log.error("Nothing founded, try with another address.")
    return render_template("index.html")
