from flask import Blueprint, request, flash, render_template, redirect, url_for

from CabotAtHome.site import app
from CabotAtHome.site.models import Group

blueprint = Blueprint("root", __name__)


@app.context_processor
def injectLinks():
    # Inject main menu links into every template render automatically
    return dict(
        links=[
            ("Home", "/"),
            ("Sign Up", "/register"),
            ("Camp Timetable", "/timetable"),
            ("Gallery", "/gallery"),
        ]
    )


@blueprint.route("/")
def index():
    return render_template("index.jinja")


@blueprint.route("/organisation")
def information():
    return render_template("information.jinja")


@blueprint.route("/register")
def register():
    return render_template("registration.jinja")


@blueprint.route("/timetable")
def timetable():
    return render_template("timetable.jinja")


@blueprint.route("/live")
def live():
    return render_template("live.jinja")
