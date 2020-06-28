from flask import Blueprint, request, flash, render_template, redirect, url_for

from app.models import Group

blueprint = Blueprint("root", __name__)


@blueprint.context_processor
def injectLinks():
    # Inject main menu links into every template render automatically
    return dict(
        links=[
            ("Home", url_for("root.index")),
            ("Sign Up", url_for("root.register")),
            ("Camp Timetable", url_for("root.timetable")),
            ("Gallery", url_for("share.gallery")),
        ]
    )


@blueprint.route("/")
def index():
    return render_template("root/index.jinja")


@blueprint.route("/organisation")
def information():
    return render_template("root/information.jinja")


@blueprint.route("/register")
def register():
    return render_template("root/registration.jinja")


@blueprint.route("/timetable")
def timetable():
    return render_template("root/timetable.jinja")


@blueprint.route("/live")
def live():
    return render_template("root/live.jinja")
