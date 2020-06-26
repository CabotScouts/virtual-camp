import os
from pathlib import Path
from flask import (
    current_app,
    Blueprint,
    request,
    flash,
    render_template,
    redirect,
    url_for,
)
from werkzeug.utils import secure_filename

from CabotAtHome.site import db
from CabotAtHome.site.models import Share, Group
from CabotAtHome.site.utils import allowedFile, getFileExtension

blueprint = Blueprint("share", __name__)


@blueprint.route("/share", methods=["GET"])
def new():
    groups = Group.query.all()
    return render_template("send-photo.jinja", groups=groups)


@blueprint.route("/share", methods=["POST"])
def upload():
    if "group" not in request.form:
        flash(
            "<i class=\"fas fa-exclamation-circle pr-2\"></i>You didn't tell us which Scout Group you're in!",
            "danger",
        )
        return redirect(request.url)

    group = Group.query.filter_by(id=request.form["group"]).first()

    if not group:
        flash(
            '<i class="fas fa-exclamation-circle pr-2"></i>There\'s something wrong with the Group you chose, please try to share your file again',
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
        s = Share(
            name=request.form["name"],
            ip=request.remote_addr,
            comment=request.form["comment"],
            group_id=group.id,
            ext=getFileExtension(file.filename),
        )
        filename = secure_filename(s.file)
        file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename,))
        db.session.add(s)
        db.session.commit()

        flash(
            '<i class="fas fa-paper-plane pr-2"></i>Your picture or video has been saved, keep your eyes peeled for it on the live stream and in our <span class="wow">Way Out West!</span> gallery!',
            "success",
        )
        return redirect(url_for("share.new"))


@blueprint.route("/gallery", defaults={"page": 0})
@blueprint.route("/gallery/<int:page>")
def gallery(page):
    # shares = Share.query.filter_by(approved=True, gallery=True)
    shares = Share.query.all()
    return render_template("gallery.jinja", shares=shares, page=page)
