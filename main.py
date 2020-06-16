from flask import Flask, session, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.jinja")


@app.errorhandler(404)
def notFoundError(error):
    return render_template("error.jinja"), 404
