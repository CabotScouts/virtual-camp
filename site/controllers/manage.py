from flask import Blueprint, request, flash, render_template, redirect, url_for
from flask_login import current_user

from CabotAtHome.site.auth import needs_manage, needs_admin
from CabotAtHome.site.models import User, Group, Share

blueprint = Blueprint("manage", __name__, url_prefix="/manage")


@blueprint.route("", strict_slashes=False)
@needs_manage
def index():
    shares = Share.query.filter_by(approved=False).order_by(Share.id)
    groups = Group.query.all()
    return render_template("admin/index.jinja", shares=shares, groups=groups)


@blueprint.route("/users")
@needs_admin
def users():
    users = User.query.filter_by(group=None)
    return render_template("admin/users.jinja", users=users)


@blueprint.route("/users/add", methods=["POST"])
@needs_admin
def addUser():
    users = User.query.filter_by(group=None)
    return redirect(url_for("manage.users"))


@blueprint.route("users/regenerate-key/<int:id>")
@needs_admin
def regenerateKey(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        flash(f"Unknown user <#{id}>", "danger")
        return redirect(url_for("manage.users"))

    if user.id == current_user.id:
        flash("You can't regenerate your own key", "danger")
        return redirect(url_for("manage.users"))

    return redirect(url_for("manage.users"))


@blueprint.route("/groups")
@needs_manage
def groups():
    groups = Group.query.all()
    return render_template("admin/groups.jinja", groups=groups)
