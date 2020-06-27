from flask import Blueprint, request, flash, render_template, redirect, url_for

from CabotAtHome.site.auth import needs_manage, needs_admin
from CabotAtHome.site.models import User, Group, Share

blueprint = Blueprint("admin", __name__, url_prefix="/admin")


@blueprint.route("", strict_slashes=False)
@needs_manage
def index():
    shares = Share.query.filter_by(approved=False).order_by(Share.id)
    groups = Group.query.all()
    return render_template("admin/index.jinja", shares=shares, groups=groups)


@blueprint.route("/users")
@needs_admin
def users():
    users = User.query.all()
    return render_template("admin/users.jinja", users=users)
