from flask import Blueprint, request, flash, render_template, redirect, url_for
from flask_login import current_user, login_required, login_user, logout_user

from CabotAtHome.site import app
from CabotAtHome.site import login_manager
from CabotAtHome.site.models import User
from CabotAtHome.site.models.User import Permission

blueprint = Blueprint("auth", __name__)

login_manager.login_view = "auth.login"


@app.context_processor
def injectAuthChecks():
    def hasAdmin():
        return current_user.hasPermission(Permission.ADMIN)

    def hasManage():
        return current_user.hasPermission(Permission.MANAGE)

    return dict(hasAdmin=hasAdmin, hasManage=hasManage)


@app.template_filter("roleName")
def roleName(role):
    roles = {0: "Guest", 1: "User", 3: "Manager", 7: "Admin"}
    return roles[role] if role in roles else "UNKNOWN"


@login_manager.user_loader
def loadUser(id):
    return User.query.get(id)


@blueprint.route("/login", methods=["GET"])
def login():
    return render_template("auth/login.jinja")


@blueprint.route("/login", methods=["POST"])
def processLogin():
    u = User.query.filter_by(username=request.form["user"]).first()
    if u and (u.key == request.form["key"]):
        login_user(u)
        flash("Successfully logged in", "success")
        return redirect(url_for("root.index"))

    else:
        flash("Username or key incorrect", "danger")
        return redirect(url_for("auth.login"))


@blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("root.index"))
