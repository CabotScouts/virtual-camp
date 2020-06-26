from flask import Blueprint, request, flash, render_template, redirect, url_for
from werkzeug.utils import secure_filename

from CabotAtHome.site import links
from CabotAtHome.site.models import Group, Share
from CabotAtHome.site.utils import allowedFile

blueprint = Blueprint("root", __name__)


@blueprint.route("/")
def index():
    return render_template("index.jinja", links=links)


@blueprint.route("/organisation")
def information():
    return render_template("information.jinja", links=links)


@blueprint.route("/register")
def register():
    return render_template("registration.jinja", links=links)


@blueprint.route("/timetable")
def timetable():
    return render_template("timetable.jinja", links=links)


@blueprint.route("/live")
def live():
    return render_template("live.jinja", links=links)


@blueprint.route("/share", methods=["GET"])
def shareForm():
    return render_template("send-photo.jinja", links=links)


@blueprint.route("/share", methods=["POST"])
def shareProcess():
    if "group" not in request.form:
        flash(
            "<i class=\"fas fa-exclamation-circle pr-2\"></i>You didn't tell us which Scout Group you're in!",
            "danger",
        )
        return redirect(request.url)

    if "file" not in request.files or request.files["file"].filename == "":
        flash(
            '<i class="fas fa-exclamation-circle pr-2"></i>You didn\'t chose a picture or video file to share with us',
            "danger",
        )
        return redirect(request.url)

    file = request.files["file"]
    valid = allowedFile(file.filename)

    if not valid:
        flash(
            "<i class=\"fas fa-exclamation-circle pr-2\"></i>The file you've tried to share isn't a valid picture or video file",
            "danger",
        )
        return redirect(request.url)

    if file and valid:
        s = Store()
        file.save(os.path.join(app.config["UPLOAD_FOLDER"],))

        flash(
            '<i class="fas fa-paper-plane pr-2"></i>Your picture or video has been saved, keep your eyes peeled for it on the live stream!',
            "success",
        )
        return redirect(url_for("index"))


@blueprint.route("/gallery", defaults={"page": 0})
@blueprint.route("/gallery/<int:page>")
def gallery(page):
    shares = Share.query.filter_by(approved=True, gallery=True)
    return render_template("gallery.jinja", links=links, shares=shares, page=page)
