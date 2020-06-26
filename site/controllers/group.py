from flask import Blueprint, request, render_template

from CabotAtHome.site.models import Group

blueprint = Blueprint("group", __name__)
prefix = "/group"


@blueprint.route("/")
def index():
    pass


@blueprint.route("/login", methods=["GET"])
def login():
    # groups = Group.query.all()
    group = request.args.get("group", "")
    key = request.args.get("key", "")
    return render_template("group/login.jinja", group=group, key=key)


@blueprint.route("/login", methods=["POST"])
def processLogin():
    pass
