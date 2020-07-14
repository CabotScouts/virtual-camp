from flask import (
    Blueprint,
    request,
    flash,
    render_template,
    redirect,
    url_for,
)

blueprint = Blueprint("activities", __name__, url_prefix="/activities")


@blueprint.route("/")
def index():
    return render_template("activities/index.jinja")


@blueprint.route("beavers")
def beavers():
    return render_template("activities/beavers.jinja")


@blueprint.route("cubs")
def cubs():
    return render_template("activities/cubs.jinja")


@blueprint.route("scouts")
def scouts():
    return render_template("activities/scouts.jinja")


@blueprint.route("explorers-network")
def explorers():
    return render_template("activities/explorers.jinja")
