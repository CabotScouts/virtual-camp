from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = False

from CabotAtHome.site.models import User, Group, Share

links = [
    ("Home", "/"),
    ("Information", "/information"),
    ("Sign Up", "/register"),
    ("Camp Timetable", "/timetable"),
]

# Static Pages
@app.route("/")
def index():
    return render_template("index.jinja", links=links)


@app.route("/information")
def information():
    return render_template("information.jinja", links=links)


@app.route("/register")
def register():
    return render_template("registration.jinja", links=links)


@app.route("/timetable")
def timetable():
    return render_template("timetable.jinja", links=links)


@app.route("/share", methods=["GET"])
def shareForm():
    return render_template("send-photo.jinja", links=links)


@app.route("/share", methods=["POST"])
def shareProcess():
    # return render_template("process-photo.jinja", links=links)
    return jsonify(request.form)


@app.route("/live")
def live():
    return render_template("live.jinja", links=links)


# Auth Pages
@app.route("/login", methods=["GET"])
def groupLoginForm():
    pass


@app.route("/login", methods=["POST"])
def groupLogin():
    pass


# Error Handlers
@app.errorhandler(404)
def notFoundError(error):
    return render_template("error.jinja", links=links, error=error), 404


@app.errorhandler(504)
def serverError(error):
    return render_template("error.jinja", links=links, error=error), 500
