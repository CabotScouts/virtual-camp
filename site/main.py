from flask import Flask, session, render_template

app = Flask(__name__)

links = [
    ("Home", "/"),
    ("Information", "/information"),
    ("Sign Up", "/register"),
    ("Camp Timetable", "/timetable"),
]


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


@app.route("/send", methods=["GET"])
def sendForm():
    return render_template("send-photo.jinja", links=links)


@app.route("/send", methods=["POST"])
def sendProcess():
    return render_template("process-photo.jinja", links=links)


@app.route("/live")
def live():
    return render_template("live.jinja", links=links)


@app.errorhandler(404)
def notFoundError(error):
    return render_template("error.jinja", links=links, error=error), 404


@app.errorhandler(504)
def serverError(error):
    return render_template("error.jinja", links=links, error=error), 500
