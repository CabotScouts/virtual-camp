from flask import (
    Blueprint,
    request,
    flash,
    render_template,
    redirect,
    url_for,
)

blueprint = Blueprint("activities", __name__, url_prefix="/activities")


@blueprint.route("")
def index():
    return render_template("activities/index.jinja")


@blueprint.route("/trail")
def trail():
    return render_template("activities/trail.jinja")
