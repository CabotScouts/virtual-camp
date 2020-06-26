from flask import Blueprint, request, render_template
from flask_login import login_user, logout_user

from CabotAtHome.site.models import Group

blueprint = Blueprint("group", __name__)
prefix = "/group"


@blueprint.route("/")
def index():
    pass


@blueprint.route("/login")
def login():
    groups = Group.query.all()
    return render_template("group/login.jinja", groups=groups)


@blueprint.route("/login", methods=["POST"])
def processLogin():
    pass


@blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("root.index"))
