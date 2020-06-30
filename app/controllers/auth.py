from flask import Blueprint, request, flash, render_template, redirect, url_for
from flask_login import current_user, login_required, login_user, logout_user

from app import login_manager, limiter
from app.models import User, Permission

blueprint = Blueprint("auth", __name__)

login_manager.login_view = "auth.login"


@blueprint.app_context_processor
def injectAuthChecks():
    def hasAdmin():
        return current_user.hasPermission(Permission.ADMIN)

    def hasManage():
        return current_user.hasPermission(Permission.MANAGE)

    def hasCurate():
        return current_user.hasPermission(Permission.CURATE)

    def hasLogin():
        return current_user.hasPermission(Permission.LOGIN)

    return dict(
        hasAdmin=hasAdmin, hasManage=hasManage, hasCurate=hasCurate, hasLogin=hasLogin
    )


@blueprint.app_template_filter("roleName")
def roleName(role):
    roles = {0: "Guest", 1: "User", 3: "Curator", 7: "Manager", 15: "Admin"}
    return roles[role] if role in roles else "UNKNOWN"


@login_manager.user_loader
def loadUser(id):
    return User.query.get(id)


@blueprint.route("/login")
@limiter.limit("10/minute")
@limiter.limit("50/hour")
def login():
    if current_user.is_authenticated and current_user.hasPermission(Permission.LOGIN):
        return redirect(url_for("manage.index"))
    else:
        return render_template("auth/login.jinja")


@blueprint.route("/login", methods=["POST"])
@limiter.limit("5/minute")
@limiter.limit("25/hour")
def processLogin():
    username = request.form["user"].lower()
    u = User.query.filter_by(username=username).first()

    if u and not u.hasPermission(Permission.LOGIN):
        flash("This user is not permitted to login", "danger")
        return redirect(url_for("auth.login"))

    if u and u.validateKey(request.form["key"]):
        login_user(u)
        flash("Successfully logged in", "success")
        return redirect(url_for("manage.index"))

    else:
        flash("Username or key incorrect", "danger")
        return redirect(url_for("auth.login"))


@blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("root.index"))
