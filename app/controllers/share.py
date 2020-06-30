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
    send_from_directory,
    abort,
)
from flask_login import current_user

from app import db
from app.models import Share, Group, Permission
from app.utils import allowedFile, getFileExtension

blueprint = Blueprint("share", __name__, url_prefix="/share")


@blueprint.route("", methods=["GET"])
def new():
    groups = Group.query.all()
    return render_template("share/new.jinja", groups=groups)


@blueprint.route("", methods=["POST"])
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
        file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], s.file))
        db.session.add(s)
        db.session.commit()

        flash(
            '<i class="fas fa-paper-plane pr-2"></i>Your picture or video has been saved, keep your eyes peeled for it on the live stream and in our <span class="wow">Way Out West!</span> gallery!',
            "success",
        )
        return redirect(url_for("share.new"))


@blueprint.route("/view/<path:image>")
def get(image):
    share = Share.query.filter_by(file=image).first_or_404()

    if (
        share.featured
        or (
            share.approved
            and current_user.hasPermission(Permission.GROUP)
            and current_user.group_id == share.group_id
        )
        or (share.approved and current_user.hasPermission(Permission.CURATE))
        or current_user.hasPermission(Permission.MANAGE)
    ):
        path = os.path.join(os.getcwd(), current_app.config["UPLOAD_FOLDER"])
        return send_from_directory(path, share.file)

    else:
        abort(403)


@blueprint.route("/gallery")
@blueprint.route("/gallery/<int:page>")
def gallery(page=0):
    shares = (
        Share.query.filter_by(approved=True, featured=True)
        .order_by(Share.id.desc())
        .paginate(page, 20, False)
    )
    return render_template("share/gallery.jinja", shares=shares)


@blueprint.route("/featured/<int:id>")
def featured(id):
    share = Share.query.filter_by(approved=True, featured=True, id=id).first_or_404()
    return render_template("share/featured.jinja", share=share)
