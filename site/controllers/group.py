from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user

from CabotAtHome.site import app
from CabotAtHome.site.models import Group, Share
from CabotAtHome.site.models.User import Permission
from CabotAtHome.site.auth import needs_group

blueprint = Blueprint("group", __name__, url_prefix="/group")


@app.context_processor
def injectAuthChecks():
    def hasGroup():
        return current_user.hasPermission(Permission.GROUP)

    return dict(hasGroup=hasGroup)


@blueprint.route("")
@blueprint.route("/<int:page>")
@needs_group
def index(page=1):
    shares = (
        Share.query.filter_by(approved=True, group_id=current_user.group.id)
        .order_by(Share.id.desc())
        .paginate(page, 12, False)
    )
    return render_template("group/index.jinja", group=current_user.group, shares=shares)


@blueprint.route("/login")
def login():
    groups = Group.query.all()
    return render_template("group/login.jinja", groups=groups)


@blueprint.route("/login", methods=["POST"])
def processLogin():
    g = Group.query.filter_by(id=request.form["group"]).first()
    if g and (g.user.key == request.form["key"]):
        login_user(g.user)
        flash("Successfully logged in", "success")
        return redirect(url_for("group.index"))

    else:
        flash("Username or key incorrect", "danger")
        return redirect(url_for("group.login"))


@blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("root.index"))
