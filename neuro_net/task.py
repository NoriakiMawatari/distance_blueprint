import json
import logging as log
from typing import Union

from decouple import config
from flask import Blueprint, redirect, render_template, request
from yandex_geocoder import Client, NothingFound

distance = Blueprint("distance", __name__, url_prefix="/distance")


@distance.route("/<address>")
def distance_to(address: str) -> str:
    error = None
    if not address:
        error = "Address needed."
        log.error(error)
    log.info(f"Given address: {address}")
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
            return redirect("/")
    return render_template("index.html")


@distance.route("/<address>/results", methods=["POST"])
def get_distance(address: str) -> Union[str, None]:
    if request.method == "POST":
        json_data = request.json
        if json_data["distance"] == "None" or json_data["time"] == "None":
            log.error("Address inside Moscow Ring Road, plese try again.")
            return json.dumps({"distance": None, "time": None})
        log.info(f"Distance from {address} to MKAD: {json_data['distance']}")
        log.info(f"Estimated travel time: {json_data['time']}")
    return json.dumps(
        {"distance": json_data["distance"], "travel_time": json_data["time"]}
    )
