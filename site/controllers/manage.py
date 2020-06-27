import os

from flask import (
    current_app,
    Blueprint,
    request,
    flash,
    render_template,
    redirect,
    url_for,
)
from flask_login import current_user

from CabotAtHome.site import app, db
from CabotAtHome.site.auth import needs_manage, needs_admin
from CabotAtHome.site.models import User, Group, Share

blueprint = Blueprint("manage", __name__, url_prefix="/manage")

sharesPerPage = 20


@app.context_processor
def injectShareCounts():
    def totalCount():
        return Share.query.count()

    def approvedCount():
        return Share.query.filter_by(approved=True, flagged=False).count()

    def pendingCount():
        return Share.query.filter_by(approved=False, flagged=False).count()

    def flaggedCount():
        return Share.query.filter_by(flagged=True).count()

    def starredCount():
        return Share.query.filter_by(starred=True).count()

    return dict(
        totalCount=totalCount,
        approvedCount=approvedCount,
        pendingCount=pendingCount,
        flaggedCount=flaggedCount,
        starredCount=starredCount,
    )


@blueprint.route("", strict_slashes=False)
@needs_manage
def index():
    return render_template("admin/index.jinja")


# Shares
@blueprint.route("/shares")
@blueprint.route("/shares/<int:page>")
@needs_manage
def allShares(page=1):
    title = "All Shares"
    shares = Share.query.order_by(Share.id.desc()).paginate(page, sharesPerPage, False)
    return render_template("admin/shares.jinja", title=title, shares=shares)


@blueprint.route("/shares/view/<int:id>")
@needs_manage
def viewShare(id):
    share = Share.query.filter_by(id=id).first_or_404()
    return render_template("admin/view-share.jinja", share=share)


@blueprint.route("/shares/approved")
@blueprint.route("/shares/approved/<int:page>")
@needs_manage
def approvedShares(page=1):
    title = "Approved Shares"
    shares = (
        Share.query.filter_by(approved=True, flagged=False)
        .order_by(Share.id.desc())
        .paginate(page, sharesPerPage, False)
    )
    return render_template("admin/shares.jinja", title=title, shares=shares)


@blueprint.route("/shares/pending")
@blueprint.route("/shares/pending/<int:page>")
@needs_manage
def pendingShares(page=1):
    title = "Pending Shares"
    shares = (
        Share.query.filter_by(approved=False, flagged=False)
        .order_by(Share.id.asc())
        .paginate(page, sharesPerPage, False)
    )
    return render_template("admin/shares.jinja", title=title, shares=shares)


@blueprint.route("/shares/flagged")
@blueprint.route("/shares/flagged/<int:page>")
@needs_manage
def flaggedShares(page=1):
    title = "Flagged Shares"
    shares = (
        Share.query.filter_by(flagged=True)
        .order_by(Share.id.asc())
        .paginate(page, sharesPerPage, False)
    )
    return render_template("admin/shares.jinja", title=title, shares=shares)


@blueprint.route("/shares/starred")
@blueprint.route("/shares/starred/<int:page>")
@needs_manage
def starredShares(page=1):
    title = "Starred Shares"
    shares = (
        Share.query.filter_by(starred=True)
        .order_by(Share.id.asc())
        .paginate(page, sharesPerPage, False)
    )
    return render_template("admin/shares.jinja", title=title, shares=shares)


# Share Modifiers
@blueprint.route("/shares/approve", methods=["POST"])
@needs_manage
def approveShare():
    share = Share.query.filter_by(id=request.form["id"]).first()
    if share:
        share.approve()
        flash("Share approved", "success")
    else:
        flash("Share not found", "danger")

    return redirect(request.referrer)


@blueprint.route("/shares/flag", methods=["POST"])
@needs_manage
def flagShare():
    share = Share.query.filter_by(id=request.form["id"]).first()
    if share:
        share.flag()
        flash("Share flagged", "warning")
    else:
        flash("Share not found", "danger")

    return redirect(request.referrer)


@blueprint.route("/shares/star", methods=["POST"])
@needs_manage
def starShare():
    share = Share.query.filter_by(id=request.form["id"]).first()
    if share:
        starred = share.star()
        if starred:
            flash("Share starred", "info")
        else:
            flash("Share unstarred", "warning")
    else:
        flash("Share not found", "danger")

    return redirect(request.referrer)


@blueprint.route("/shares/delete", methods=["POST"])
@needs_admin
def deleteShare():
    share = Share.query.filter_by(id=request.form["id"]).first()
    if share:
        path = os.path.join(
            os.getcwd(), current_app.config["UPLOAD_FOLDER"], share.file
        )
        if os.path.isfile(path):
            os.remove(path)

        # TODO: turn this into a soft delete (so we retain time & IP)
        db.session.delete(share)
        db.session.commit()
        flash("Share removed", "warning")
    else:
        flash("Share not found", "danger")
    # For deletes from the single view page this will 404 for now
    return redirect(request.referrer)


# Groups/Users
@blueprint.route("/users")
@needs_admin
def users():
    users = User.query.filter_by(group=None).order_by(User.username)
    return render_template("admin/users.jinja", users=users)


@blueprint.route("/users/add", methods=["POST"])
@needs_admin
def addUser():
    user = User.query.filter_by(username=request.form["username"]).first()

    if user:
        flash("A user with that name already exists", "danger")
        return redirect(url_for("manage.users"))

    if request.form["username"] == "":
        flash("A username is required", "danger")
        return redirect(url_for("manage.users"))

    new = User(username=request.form["username"], role=request.form["role"])
    db.session.add(new)
    db.session.commit()

    return redirect(url_for("manage.users"))


@blueprint.route("users/regenerate-key", methods=["POST"])
@needs_admin
def regenerateKey():
    id = request.form["id"]

    user = User.query.filter_by(id=id).first()
    if not user:
        flash(f"Unknown user <#{id}>", "danger")
        return redirect(url_for("manage.users"))

    if user.id == current_user.id:
        flash("You can't regenerate your own key", "danger")
        return redirect(url_for("manage.users"))

    user.generateKey()
    db.session.add(user)
    db.session.commit()
    flash(f"Regenerated key for { user.name }", "success")
    next = "manage.groups" if request.form["return"] == "group" else "manage.users"
    return redirect(url_for(next))


@blueprint.route("users/update-role", methods=["POST"])
@needs_admin
def updateRole():
    id = request.form["id"]

    user = User.query.filter_by(id=id).first()
    if not user:
        flash(f"Unknown user <#{id}>", "danger")
        return redirect(url_for("manage.users"))

    if user.id == current_user.id:
        flash("You can't change your own role", "danger")
        return redirect(url_for("manage.users"))

    user.role = request.form["role"]
    db.session.add(user)
    db.session.commit()
    flash(f"Updated role for { user.name }", "success")
    return redirect(url_for("manage.users"))


@blueprint.route("users/delete", methods=["POST"])
@needs_admin
def deleteUser():
    id = request.form["id"]

    user = User.query.filter_by(id=id).first()
    if not user:
        flash(f"Unknown user <#{id}>", "danger")
        return redirect(url_for("manage.users"))

    if user.id == current_user.id:
        flash("You can't delete yourself", "danger")
        return redirect(url_for("manage.users"))

    db.session.delete(user)
    db.session.commit()
    flash(f"Removed { user.name }", "warning")
    return redirect(url_for("manage.users"))


@blueprint.route("/groups")
@needs_manage
def groups():
    groups = Group.query.all()
    return render_template("admin/groups.jinja", groups=groups)
