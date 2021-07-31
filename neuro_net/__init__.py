import logging as log

from flask import Flask, redirect, render_template, request
from flask.helpers import flash

__version__ = "0.1.0"


def create_app() -> Flask:
    """App factory, logging configurations and app route(s) instances."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="secret")
    log.basicConfig(
        filename="demo.log",
        level=log.INFO,
        format="%(asctime)s :: %(levelname)s :: %(message)s",
    )

    @app.route("/", methods=["GET", "POST"])
    def index() -> str:
        """Specified address sent to a blueprint (/distance)
        and validation of address is executed."""
        if request.method == "POST":
            error = None
            address = request.form["address"]
            if not address:
                error = "Address required to complete task."
            if error is None:
                try:
                    return redirect(f"/distance/{address}")
                except BaseException as err:
                    log.error(f"[INVALID ADDRESS] - {err}!!!!!")
            flash(error)
        return render_template("index.html")

    # Register blueprint
    from .task import distance

    app.register_blueprint(distance)
    return app
